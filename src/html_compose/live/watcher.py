import glob
import os
import re
import stat
import subprocess
from fnmatch import fnmatch
from threading import Thread
from time import sleep, time
from typing import Callable, Optional, Union

try:
    import pyinotify
except ImportError:
    pyinotify = None


class ShellCommand:
    def __init__(
        self, command: Union[str, list[str]], env: Optional[list[str]] = None
    ):
        self.command = command
        self.env = os.environ.copy()


class WatchCond:
    """
    A condition for watching file(s) and trigger action.
    """

    def __init__(
        self,
        path_glob: Union[str, list[str]],
        action: Union[ShellCommand, Callable],
        ignore_glob: Optional[Union[str, list[str]]] = None,
        delay: float = 0,
    ):
        """
        Initialize a WatchCond.

        :param path_glob: Glob pattern(s) to watch for changes.
        :param action: Action to run when a change is detected. Shell command or function.
        :param ignore_glob: Glob patterns to ignore.
        :param delay: Delay in seconds before running the action after a change.


                      The timer resets after each change.
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
        self.action = action
        self.delay = delay
        self.update_count = 0
        self.process: Optional[subprocess.Popen] = None

    def try_path_hit(self, path: str) -> bool:
        """Check if a given path matches any of the glob patterns."""

        for glob_pattern in self.ignore_glob:
            if fnmatch(path, glob_pattern):
                return True

        for glob_pattern in self.path_glob:
            if fnmatch(path, glob_pattern):
                return True

        return False

    def run(self):
        """Run the action for changes."""

        def _run(update_id):
            # Delay mechanism:
            # We sleep for small periods before running the action
            # If the hit mechanism fires in the middle of a delay,
            # we just stop.
            if self.delay:
                delay = self.delay
                start = time()
                while delay > 2 and self.update_count == update_id:
                    now = time()
                    delay -= now - start
                    start = now
                    sleep(1)

                if self.delay > 0:
                    sleep(self.delay)

                if self.update_count != update_id:
                    # Let someone else start a delay thread
                    return

            if self.process:
                self.process.terminate()
                # Wait on the process to actually end
                self.process.wait()

            if callable(self.action):
                self.action()
            else:
                self.process = subprocess.Popen(
                    self.action.command, shell=True, env=self.action.env
                )

        if self.delay > 0:
            Thread(target=_run, args=(self.update_count,), daemon=True).start()
        else:
            _run(self.update_count)


class Hit:
    def __init__(self, path: str, conds: list[WatchCond]):
        self.path = path
        self.conds = conds


class Watcher:
    """Simple file watcher with support for both stat and inotify."""

    def __init__(self, conds: list[WatchCond], no_inotify=False):
        self.mtimes = {}
        self.changes = []
        self.conds = conds
        self.watch_globs = []
        self.inotify_paths = set()
        self.notifier = None
        # Setup inotify if available
        self.has_inotify = pyinotify is not None and not no_inotify
        if self.has_inotify:
            self.wm = pyinotify.WatchManager()
            self.notifier = None
            self._setup_inotify()
        for cond in conds:
            for g in cond.path_glob:
                self.add_pattern(g)

        if self.has_inotify:
            self._watch_inotify()
            pass

    def overhead(self):
        if self.has_inotify:
            recursive_count = 0
            dirs = set()
            for wglob, recursive in self.inotify_paths:
                if recursive:
                    recursive_count += 1
                dirs.add(wglob)
            return {
                "path_count": len(dirs),
                "recursive_count": recursive_count,
                "paths": dirs,
            }
        else:
            paths = list(self._resolve_paths())
            return {"path_count": len(list(paths)), "paths": paths}

    def _setup_inotify(self):
        """Setup inotify event handler."""

        class EventHandler(pyinotify.ProcessEvent):
            def __init__(self, watcher: Watcher):
                self.watcher = watcher

            def process_default(self, event):
                if not event.dir and os.path.isfile(event.pathname):
                    rule_hits = self.watcher._get_matching_rules(event.pathname)
                    if rule_hits:
                        self.watcher.changes.append(
                            Hit(event.pathname, rule_hits)
                        )

        self.handler = EventHandler(self)
        self.notifier = pyinotify.ThreadedNotifier(self.wm, self.handler)
        self.notifier.start()

    def _watch_inotify(self):
        for wglob in self.watch_globs:
            recursive = False
            if wglob.endswith("/"):
                recursive = True
            re_parse = re.search(r"^(.*)[*]{2}", wglob)
            if re_parse:
                wglob = re_parse.group(1)
                recursive = True
            if not recursive:
                wglob = os.path.dirname(wglob)
                if not wglob:
                    wglob = "."
            as_t = (wglob, recursive)
            if as_t in self.inotify_paths:
                continue

            self.inotify_paths.add(as_t)
            mask = (
                pyinotify.IN_MODIFY | pyinotify.IN_CREATE | pyinotify.IN_DELETE
            )
            self.wm.add_watch(wglob, mask, do_glob=True, rec=recursive)

    def add_pattern(self, pattern):
        """Add a glob pattern to watch."""

        # Add to inotify if possible
        if self.has_inotify:
            # Extract directory part from glob
            dir_path = os.path.dirname(pattern)
            if not dir_path:
                dir_path = "."

            if dir_path in self.watch_globs:
                # Already watching, ignore
                return
            self.watch_globs.append(pattern)
            # Watch the directory containing the glob
            mask = (
                pyinotify.IN_MODIFY | pyinotify.IN_CREATE | pyinotify.IN_DELETE
            )
            self.wm.add_watch(dir_path, mask, do_glob=True, rec=True)
        else:
            self.watch_globs.append(pattern)

    def _get_matching_rules(self, path) -> Optional[list[WatchCond]]:
        """Find the first glob pattern that matches the path."""
        rules = []
        for cond in self.conds:
            # Check if the path matches the glob pattern
            if cond.try_path_hit(path):
                rules.append(cond)

        return rules if rules else None

    def _resolve_paths(self):
        """Resolve all glob patterns to file paths."""

        # Add all files matching watch patterns
        for pattern in self.watch_globs:
            for match in glob.iglob(pattern, recursive=True):
                for cond in self.conds:
                    if cond.try_path_hit(match):
                        yield match

    def changed(self) -> list[Hit]:
        """Check if any watched files have changed.

        Returns (path, matching_glob) if a change was detected, None otherwise.
        """
        # Return any queued inotify changes first
        if self.changes:
            changes = self.changes
            self.changes = []

            return changes

        # Don't stat if inotify is available and just had nothing
        if self.has_inotify:
            return

        # Fall back to stat-based checking
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
                mtime = st.st_mtime
            except OSError:
                # Might be deleted, we'll catch it later
                continue

            current_mtimes[path] = mtime
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
