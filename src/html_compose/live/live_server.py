from socket import create_connection
from socket import timeout as socket_timeout
from time import sleep, time

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


def _wait_for_server(
    host: str, port: int, timeout: float, daemon_task: ProcessTask
) -> None:
    start_time = time()
    print(f"Waiting for server at {host}:{port} to come online...")
    while time() - start_time < timeout:
        try:
            with create_connection((host, port), timeout=1):
                print(f"{host}:{port} is online.")
                return
        except (ConnectionRefusedError, socket_timeout):
            sleep(0.25)

    daemon_task.cancel()
    daemon_task.canceling = False  # this is an early term

    raise RuntimeError(
        f"Unable to reach {host}:{port} after {int(timeout)} seconds."
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
    daemon_host: str | None = None,
    daemon_port: int | None = None,
    daemon_timeout: float = 30.0,
    proxy_host: str | None = None,
    proxy_uri: str | None = None,
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
    :type conds: list[WatchCond]

    :param force_polling: Force slow stat() polling backend - useful if your platform is unable to support OS based watching.
    :type force_polling: bool

    :param host: Host for livereload server websocket to listen on
    :type host: str

    :param port: Port for livereload server websocket to listen on
    :type port: int

    :param print_paths: Enumerate paths being monitored
    :type print_paths: bool

    :param loop_delay: Set delay between checks for changes. Usually unnecessary.
    :type loop_delay: float

    :param livereload_delay: Delay livereload server update until x seconds after daemon update
    :type livereload_delay: float

    :param daemon_host: Host the HTTP server daemon listens on. Used to determine when the server is back up.
    :type daemon_host: str | None

    :param daemon_port: Port the HTTP server daemon listens on. Used to determine when the server is back up.
    :type daemon_port: int | None

    :param daemon_timeout: Timeout in seconds to wait for daemon port to come online after restart.
    :type daemon_timeout: int | None

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
    daemon_stop_task = Task(action=lambda: daemon_task.cancel(), sync=True)
    # Run livereload server
    server = run_server(host, port)
    tr = TaskRunner()
    tr.add_task(daemon_task)
    tr.run()  # Start task runner thread
    pending_reload: set[str] = set()

    def reload():
        changed = list(pending_reload)
        pending_reload.clear()
        if daemon_port is not None:
            # If specified, we want to wait for the listening daemon port
            # to show up before we tell the browser to reload.
            _wait_for_server(
                daemon_host or host,
                daemon_port,
                daemon_timeout,
                daemon_task=daemon_task,
            )
        reload_because(changed)

    browser_update_task = Task(reload, delay=0, sync=False)
    try:
        while True:
            if tr.cancelled:
                print("Task runner has closed. Exiting...")
                break

            if daemon_task.has_ended_early():
                status = daemon_task.status_code()
                print(
                    f"Daemon process has exited with code {status}. Exiting..."
                )
                break
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

                    # this should make them fire on the same tick, in order
                    daemon_stop_task.delay = daemon_task.delay

                    # This constant should mean the server port is up
                    browser_update_task.delay = (
                        daemon_task.delay + livereload_delay
                    )
                    print(
                        f"Reloading daemon after {daemon_task.delay} seconds..."
                    )
                    if any([c.server_reload for c in conds_hit]):
                        tr.add_task(daemon_stop_task)
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
