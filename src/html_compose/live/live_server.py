from time import sleep

from ..util_funcs import generate_livereload_env
from .watcher import ShellCommand, WatchCond, Watcher


def live_server(
    daemon: ShellCommand,
    daemon_delay: int,
    conds: list[WatchCond],
    no_inotify: bool = False,
    host="localhost",
    port="51353",
    print_paths=True,
    loop_delay=1,
) -> None:
    w = Watcher(conds, no_inotify)
    oh = w.overhead()
    if print_paths:
        for path in oh["paths"]:
            print(f"Monitoring {path}")

    if w.has_inotify:
        print(
            f"Monitoring {oh['path_count']} paths via inotify and "
            f"{oh['recursive_count']} recursive paths"
        )
    else:
        print(f"Monitoring {oh['path_count']} paths for changes via stat")

    # Set livereload environment variables
    daemon.env.update(generate_livereload_env(host, port))

    daemon_cmd = WatchCond(path_glob="", action=daemon)
    daemon_cmd.run()
    try:
        while True:
            hits = w.changed()
            if hits:
                paths_hit = set()
                conds_hit = set()
                for hit in hits:
                    paths_hit.add(hit.path)

                    for cond in hit.conds:
                        conds_hit.add(cond)

                for path in paths_hit:
                    print(f"Changed: {path}")

                delay = 0
                for cond in conds_hit:
                    delay = max(delay, cond.delay)
                    cond.run()
                daemon_cmd.delay = delay + daemon_delay
                print(f"Reloading daemon after {daemon_cmd.delay} seconds...")
                daemon_cmd.run()
            sleep(loop_delay)
    except KeyboardInterrupt:
        # Stop inotify and daemon
        if w.notifier:
            w.notifier.stop()

        if daemon_cmd.process:
            proc = daemon_cmd.process
            proc.terminate()
            proc.wait()
