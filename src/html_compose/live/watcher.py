import glob
import os
import stat
import subprocess
from pathlib import Path
from threading import RLock, Thread
from time import sleep, time
from typing import Callable

from watchfiles._rust_notify import RustNotify

from ..util_funcs import glob_matcher

CWD = Path(".").absolute()


class ShellCommand:
    def __init__(
        self, command: str | list[str], env: dict[str, str] | None = None
    ):
        self.command = command
        self.env = os.environ.copy()
        if env:
            self.env.update(env)


class Task:
    def __init__(self, action: Callable | None, delay: float = 0.0, sync=False):
        self.action = action
        self.delay = delay
        self.update_count = 0
        self.sync = sync
        self.exc: Exception | None = None
        self.complete: bool | None = None

    def active_check(self, update_id):
        return self.update_count == update_id

    def _do_run(self):
        try:
            if self.action:
                self.action()
        except Exception as e:
            self.exc = e
        self.complete = True

    def run(self):
        """
        Execute the task's action.

        If this is not a sync task it runs in a thread.

        self.exc is set if an exception occurred during execution.
        """
        self.complete = False
        if not self.action:
            return

        if self.sync:
            self._do_run()
        else:
            Thread(target=self._do_run, daemon=True).start()

    def cancel(self):
        # Implement cancellation logic here
        pass


class ProcessTask(Task):
    def __init__(self, command: ShellCommand, delay: float = 0.0, sync=False):
        self.command = command
        self.process = None
        super().__init__(self._run_process, delay, sync)
        self.canceling = False

    def _run_process(self):
        self.cancel()  # Close existing proc if it is open

        shell = isinstance(self.command.command, str)
        self.process = subprocess.Popen(
            self.command.command, shell=shell, env=self.command.env
        )

        self.canceling = False

    def cancel(self) -> None:
        if self.process:
            self.canceling = True
            # Subprocess will skip these steps if the process is already closed
            self.process.terminate()
            # Wait on the process to actually end
            try:
                self.process.wait()
            except KeyboardInterrupt:
                # This would happen on the main thread
                # The user is waiting for us to close but we're waiting on
                # a 'graceful' close.
                # The user wants us to hurry up, so kill -9 it.
                print(f"ProcessTask: sigkill for {self.command.command}.")
                self.process.kill()

    def has_ended_early(self) -> bool:
        if self.canceling:
            return False

        if self.process:
            return self.process.poll() is not None

        return False

    def status_code(self) -> int | None:
        if self.process:
            return self.process.poll()
        return None


class TaskRunner:
    def __init__(self) -> None:
        self.lock = RLock()
        self.tasks: list[tuple[int, float, Task]] = []
        self.cancelled = False
        self._thread = Thread(target=self.worker, daemon=True)

    def run(self):
        self.cancelled = False
        if not self._thread.is_alive():
            self._thread.start()

    def cancel(self):
        self.cancelled = True

    def add_task(self, task: Task):
        if not task.action:
            return

        with self.lock:
            task.update_count += 1
            self.tasks.append((task.update_count, time() + task.delay, task))

    def worker(self) -> None:
        to_remove: list[int] = []
        to_run: list[Task] = []
        running: list[Task] = []

        def _exit(exc: Exception) -> None:
            for i in running:
                i.cancel()
            self.cancel()
            raise exc

        while not self.cancelled:
            # Acquire lock to safely access shared task list.
            with self.lock:
                now = time()
                # Iterate through all pending tasks.
                for i, entry in enumerate(self.tasks):
                    update_id, due, task = entry
                    # Perform "active check" to debounce rapid events.
                    if not task.active_check(update_id):
                        to_remove.append(i)  # Mark stale task for removal.
                        continue

                    # If task is not stale and due time has passed, mark for removal and run.
                    if now >= due:
                        to_remove.append(i)
                        to_run.append(task)

                # Remove all marked (stale or due) tasks in reverse to avoid index errors.
                for i in reversed(to_remove):
                    del self.tasks[i]
                to_remove.clear()

            # Release the lock.
            # Execute all tasks to be run outside the lock to avoid blocking.
            for task in to_run:
                running.append(task)
                task.run()
                if task.sync:
                    running.remove(task)
                if task.exc:
                    _exit(exc=task.exc)

            # Check for completed async tasks.
            for i in reversed(range(len(running))):
                task = running[i]
                if task.complete:
                    del running[i]
                    if task.exc:
                        _exit(exc=task.exc)
            # Clear the to_run list for the next iteration.
            to_run.clear()

            # Sleep briefly to prevent busy-waiting and high CPU usage.
            sleep(0.1)


class WatchCond:
    """
    A condition for watching file(s) and trigger action.
    """

    def __init__(
        self,
        path_glob: str | list[str],
        action: ShellCommand | Callable | None,
        ignore_glob: str | list[str] | None = None,
        delay: float = 0,
        server_reload: bool = True,
        reload: bool = True,
    ):
        """
        Initializes a WatchCond.

        Args:
            path_glob:
                Glob pattern(s) to watch for changes.

            action:
                Action to run when a change is detected. Shell command or function.
                When action is None, no action is run but reloads may still occur.

            ignore_glob:
                Glob patterns to ignore.

            delay:
                Delay in seconds before running the action after a change.
                The timer resets after each change to de-duplicate file change events.

            reload:
                If False, neither the browser nor the server will be reloaded.
                This is useful for triggering js/css builds, which you might
                pair with a separate WatchCond on the build output directory
                that does the reloading.

            server_reload:
                If False, do not reload the daemon process after a change; just the browser.
        """
        self.path_glob = path_glob
        if isinstance(path_glob, str):
            self.path_glob = [path_glob]

        if not ignore_glob:
            ignore_glob = []

        if isinstance(ignore_glob, str):
            self.ignore_glob = [ignore_glob]
        else:
            self.ignore_glob = ignore_glob
        self.server_reload = server_reload
        self.reload = reload
        if action is None:
            self.task = Task(None, delay)
        elif isinstance(action, ShellCommand):
            self.task = ProcessTask(action, delay)
        else:
            if not callable(action):
                raise ValueError("Action must be a ShellCommand or a callable")

            self.task = Task(action, delay)

    def try_path_hit(self, path: str) -> bool:
        """Check if a given path matches any of the glob patterns."""

        for pattern in self.ignore_glob:
            if glob_matcher(pattern, path):
                return False

        for pattern in self.path_glob:
            if glob_matcher(pattern, path):
                return True

        return False


class Hit:
    def __init__(self, path: str, conds: list[WatchCond]):
        self.path = path
        self.conds = conds


class Watcher:
    """Simple file watcher with support for both stat and inotify."""

    def __init__(self, conds: list[WatchCond], force_polling: bool):
        self.conds = conds
        self.watch_globs = []
        self.mtimes: dict[str, int] = {}
        self.force_polling = force_polling

        for cond in conds:
            for g in cond.path_glob:
                self.watch_globs.append(g)

        self.rust_watches = []
        if not self.force_polling:
            recursive = []
            non_recursive = []
            for path, is_recursive in self._get_fswatch_dirs():
                if is_recursive:
                    recursive.append(path)
                else:
                    non_recursive.append(path)
            if recursive:
                rn = RustNotify(
                    recursive,
                    recursive=True,
                    debug=False,
                    force_polling=False,
                    poll_delay_ms=0,
                    ignore_permission_denied=True,
                )
                self.rust_watches.append(rn)
            if non_recursive:
                nr = RustNotify(
                    non_recursive,
                    recursive=False,
                    debug=False,
                    force_polling=False,
                    poll_delay_ms=0,
                    ignore_permission_denied=True,
                )
                self.rust_watches.append(nr)

    def overhead(self):
        if not self.force_polling:
            recursive_count = 0
            dirs = set()
            fswatch_dirs = self._get_fswatch_dirs()
            for path, recursive in fswatch_dirs:
                if recursive:
                    recursive_count += 1
                dirs.add(path)
            return {
                "path_count": len(dirs),
                "recursive_count": recursive_count,
                "paths": dirs,
            }
        else:
            paths = list(self._resolve_paths())
            return {"path_count": len(list(paths)), "paths": paths}

    def _get_fswatch_dirs(self):
        # We handle a few kinds of watch expressions:
        # dir/: Watch dir/ recursively
        # ./file.py: Watch just a single file
        # ./src/*.py: Watch ./src/ non-recursively for .py files
        # dir/**/*.py: Watch dir/ recursively
        # **/*.py: watch ./ recursively
        dirs = set()
        for cond in self.conds:
            for pattern in cond.path_glob:
                recursive = False
                if pattern.endswith("/"):
                    recursive = True

                path_component = Path(pattern)
                if "**" in path_component.parts:
                    recursive = True
                    for i, part in reversed(
                        list(enumerate(path_component.parts))
                    ):
                        if part == "**":
                            pattern = str(Path(*path_component.parts[0:i]))
                            if not pattern:
                                pattern = "."

                for p in glob.glob(pattern):
                    path = Path(p)
                    if not recursive and path.is_file():
                        # If this is a file glob, get the containing dir
                        p = path.parent

                    as_t = (str(p), recursive)
                    if as_t in dirs:
                        continue

                    dirs.add(as_t)
        return dirs

    def _get_matching_rules(self, path) -> list[WatchCond]:
        """Find the first glob pattern that matches the path."""
        rules = []
        for cond in self.conds:
            # Check if the path matches the glob pattern
            if cond.try_path_hit(path):
                rules.append(cond)

        return rules

    def _resolve_paths(self):
        """Resolve all glob patterns to file paths."""

        # Add all files matching watch patterns
        for pattern in self.watch_globs:
            for match in glob.iglob(pattern, recursive=True):
                for cond in self.conds:
                    if cond.try_path_hit(match):
                        yield match

    def stat_watcher(self):
        paths = self._resolve_paths()
        changes = []
        current_mtimes = {}
        changed = set()
        if not self.mtimes:
            current_mtimes = self.mtimes

        for path in paths:
            try:
                if path in changed:
                    # Already processed this file
                    continue

                st = os.stat(path)
                if not stat.S_ISREG(st.st_mode):
                    # Not a regular file, skip it
                    continue
                mtime = int(st.st_mtime)
            except OSError:
                # Might be deleted, we'll catch it later
                continue

            current_mtimes[path] = int(mtime)
            old_mtime = self.mtimes.get(path, None)

            if old_mtime != mtime:
                matching_rules = self._get_matching_rules(path)
                changes.append(Hit(path, matching_rules))
                changed.add(path)

        # Check for deleted files
        for path in self.mtimes.keys():
            if path not in current_mtimes:
                matching_rules = self._get_matching_rules(path)
                if matching_rules:
                    changes.append(Hit(path, matching_rules))

        self.mtimes = current_mtimes
        return changes

    def changed(self) -> list[Hit]:
        """Check if any watched files have changed.

        Returns (path, matching_glob) if a change was detected, None otherwise.
        """
        if self.force_polling:
            return self.stat_watcher()

        changes = []
        for watch in self.rust_watches:
            # Check and immediately return
            result = watch.watch(
                debounce_ms=100, step_ms=1, timeout_ms=1, stop_event=None
            )
            if result == "signal":
                # Probably a ctrl + C
                raise KeyboardInterrupt()
            if result == "timeout":
                continue
            # We don't have a stop event and that's the only other type.
            # Alas, ignore it.
            if isinstance(result, str):
                print(
                    "watcher: Not sure what to do with",
                    repr(result),
                    " submit a git issue to html-compose",
                )
                continue

            assert isinstance(result, set), (
                f"Unexpected result type: {type(result)}"
            )

            result_tuples: set[tuple[int, str]] = result
            for watch_id, path in result_tuples:
                # RustWatch returns full paths, convert to relative
                path = str(Path(path).relative_to(CWD))
                matching_rules = self._get_matching_rules(path)
                if matching_rules:
                    changes.append(Hit(path, matching_rules))

        return changes
