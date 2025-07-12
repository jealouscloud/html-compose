"""
Live server and file watcher for HTML Compose.

Automatically reloads your Python server and the browser on changes.

The typical recommendation is to write a script file to use this module.

Example:
```python
# live-reload.py
import html_compose.live as live

live.server(
    daemon=live.ShellCommand(
        "rye run flask --app  ./backend/web/server.py run"
    ),
    daemon_delay=0.2,
    conds=[
        live.WatchCond(
            path_glob="backend/**/*.py", action=live.ShellCommand("date")
        ),
        live.WatchCond(path_glob="content/blog/*.md", action=None),
        live.WatchCond(
            ["frontend/**/*.js", "frontend/**/*.css"],
            action=live.ShellCommand("cd frontend && pnpm build"),
            ignore_glob=["frontend/node_modules/"],
            reload=False,
        ),
        live.WatchCond(
            "public/**/*",
            action=None,
            server_reload=False,
        ),
    ],
    host="localhost",
    port=51353,
    livereload_delay=0.7,
)
```

"""

from .live_server import live_server
from .watcher import ShellCommand, WatchCond, Watcher

server = live_server
__all__ = ["server", "ShellCommand", "WatchCond", "Watcher"]
