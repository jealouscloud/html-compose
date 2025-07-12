from time import sleep
from typing import Optional

from ..util_funcs import generate_livereload_env
from .livereload_server import reload_because, run_server
from .watcher import (
    ProcessTask,
    ShellCommand,
    Task,
    TaskRunner,
    WatchCond,
    Watcher,
)


def live_server(
    daemon: ShellCommand,
    daemon_delay: float,
    conds: list[WatchCond],
    force_polling: bool = False,
    host: str = "localhost",
    port: int = 51353,
    print_paths=True,
    loop_delay=1,
    livereload_delay=0.2,
    proxy_host: Optional[str] = None,
    proxy_uri: Optional[str] = None,
) -> None:
    """
    Run a live-reload server that also runs and reloads your Python server.

    This is a development feature and not recommended for production use.

    Delays are deduplicated after file changes by various delay properties
    to prevent chains of restarts.

    :param daemon: Command to run in the background, typically a Python server
    :type daemon: ShellCommand
    :param daemon_delay: Delay in seconds before restarting the daemon after a change.
    :type daemon_delay: float
    :param conds: List of watch conditions, which are a path and action.
    :type conds:
    :param force_polling: Force slow stat() polling backend - useful if your platform is unable to support OS based watching.
    :type force_polling: bool
    :param host: Host for livereload server websocket to listen on
    :type host: str
    :param port: Port for livereload server websocket to listen on
    :type port: int
    :param print_paths: Enumerate paths being monitored
    :type print_paths:
    :param loop_delay: Set delay between checks for changes. Usually unnecessary.
    :type loop_delay: float
    :param livereload_delay: Delay livereload server update until x seconds after daemon update
    :type livereload_delay: float
    :param proxy_uri: If websocket is behind a reverse proxy, this is the URI to reach it by.
                      This is useful if you are developing behind SSL.
    :type proxy_uri: str
    :param proxy_host: If websocket is behind a reverse proxy, this is the host to reach it by.
                       This is useful if you are developing behind SSL.
    :type proxy_host: str
    """
    w = Watcher(conds, force_polling=force_polling)
    oh = w.overhead()
    if print_paths:
        for path in oh["paths"]:
            print(f"Monitoring for changes: {path}")

    if not w.force_polling:
        print(
            f"Monitoring {oh['path_count']} path(s) via RustNotify. "
            f"{oh['recursive_count']} path(s) are monitored recursively."
        )
    else:
        print(f"Monitoring {oh['path_count']} path(s) for changes via polling")

    # Set livereload environment variables
    daemon.env.update(
        generate_livereload_env(host, port, proxy_host, proxy_uri)
    )

    daemon_task = ProcessTask(daemon, delay=0, sync=False)
    # Run livereload server
    server = run_server(host, port)
    tr = TaskRunner()
    tr.add_task(daemon_task)
    tr.run()  # Start task runner thread
    pending_reload: set[str] = set()

    def reload():
        changed = list(pending_reload)
        pending_reload.clear()
        reload_because(changed)

    browser_update_task = Task(reload, delay=0, sync=False)
    try:
        while True:
            hits = w.changed()
            if hits:
                paths_hit = set()
                conds_hit: set[WatchCond] = set()
                for hit in hits:
                    paths_hit.add(hit.path)

                    for cond in hit.conds:
                        if cond.reload:
                            pending_reload.add(hit.path)

                        conds_hit.add(cond)

                for path in paths_hit:
                    print(f"Changed: {path}")

                delay = 0.0
                reload_tripped = False
                for cond in conds_hit:
                    if cond.task:
                        tr.add_task(cond.task)

                    if not cond.reload:
                        continue
                    delay = max(delay, cond.task.delay)
                    reload_tripped = True

                if reload_tripped:
                    daemon_task.delay = delay + daemon_delay
                    # This constant should mean the server port is up
                    browser_update_task.delay = (
                        daemon_task.delay + livereload_delay
                    )
                    print(
                        f"Reloading daemon after {daemon_task.delay} seconds..."
                    )
                    if any([c.server_reload for c in conds_hit]):
                        tr.add_task(daemon_task)
                    tr.add_task(browser_update_task)
            sleep(loop_delay)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        server.shutdown()

        for watch in w.rust_watches:
            watch.close()

        daemon_task.cancel()
        for cond in conds:
            if cond.task:
                cond.task.cancel()
