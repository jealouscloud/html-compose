from time import sleep

from ..util_funcs import generate_livereload_env
from .watcher import ShellCommand, WatchCond, Watcher


def live_server(
    daemon: ShellCommand,
    daemon_delay: float,
    conds: list[WatchCond],
    force_polling: bool = False,
    host: str = "localhost",
    port: int = 51353,
    print_paths=True,
    loop_delay=1,
) -> None:
    """
    Run a live-reload server that also runs and reloads your Python server.

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
    :type loop_delay:
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
    daemon.env.update(generate_livereload_env(host, port))

    daemon_cmd = WatchCond(path_glob="", action=daemon)
    daemon_cmd.run()
    try:
        while True:
            hits = w.changed()
            if hits:
                paths_hit = set()
                conds_hit: set[WatchCond] = set()
                for hit in hits:
                    paths_hit.add(hit.path)

                    for cond in hit.conds:
                        conds_hit.add(cond)

                for path in paths_hit:
                    print(f"Changed: {path}")

                delay = 0.0
                reload_tripped = False
                for cond in conds_hit:
                    cond.run()
                    if cond.no_reload:
                        continue
                    delay = max(delay, cond.delay)
                    reload_tripped = True

                if reload_tripped:
                    daemon_cmd.delay = delay + daemon_delay
                    print(
                        f"Reloading daemon after {daemon_cmd.delay} seconds..."
                    )
                    daemon_cmd.run()
            sleep(loop_delay)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        for watch in w.rust_watches:
            watch.close()

        if daemon_cmd.process:
            proc = daemon_cmd.process
            proc.terminate()
            proc.wait()
