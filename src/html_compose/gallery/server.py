import http.server
import importlib
import mimetypes
import os.path
import sys
import threading
from pathlib import Path
from time import sleep
from typing import cast
from urllib.parse import parse_qs, urlparse

from ..live import WatchCond, Watcher, livereload_server
from . import app
from .impl import (
    ShowcaseResult,
    env_registry,
    show_showcases,
    showcase_registry,
)


class Settings:
    resource_prefix = "/"
    static_dir = Path.cwd() / "static"

    @staticmethod
    def set_static_dir(path: str) -> None:
        Settings.static_dir = Path(path)


# Common web mimetypes if the system mimetypes db fails
WEB_MIMETYPES = {
    ".html": "text/html",
    ".css": "text/css",
    ".js": "application/javascript",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".gif": "image/gif",
    ".svg": "image/svg+xml",
}


class GalleryRequestHandler(http.server.BaseHTTPRequestHandler):
    content: list[ShowcaseResult] = []

    def _handle(self) -> None:
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)
        content = GalleryRequestHandler.content

        if path == "/" or path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(app.main_route(content).encode("utf-8"))
            return

        for c in content:
            if path == f"/showcase/{c.func_module}/{c.func_name}":
                # Filter on name if provided
                test_name = query.get("name", None)
                if test_name:
                    if c.name != test_name[0]:
                        continue

                if not c.success:
                    self.send_response(500)
                    self.send_header("Content-Type", "text/plain")
                    self.end_headers()
                    self.wfile.write(f"Showcase broken: {c.result}".encode())
                    return

                # Serve the showcase
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(app.generate_showcase(c).encode("utf-8"))
                return

        # Try to serve static files
        if self._serve_static(path):
            return

        # Nothing matched
        self.send_response(404)
        self.end_headers()

    def do_GET(self):
        # This method handles all GET requests
        self._handle()

    def _serve_static(self, path: str) -> bool:
        if not Settings.static_dir:
            return False
        prefix = Settings.resource_prefix
        if path.startswith(prefix):
            normalized = path.removeprefix(prefix).lstrip("/")
        else:
            return False

        # Collapse .. to prevent directory traversal without resolving symlinks
        candidate = Path(os.path.normpath(Settings.static_dir / normalized))

        # Not relative to static dir
        if not candidate.is_relative_to(
            Path(os.path.normpath(Settings.static_dir))
        ):
            return False

        # Resolve symlinks for the actual file read
        # as a developer server, we assume your symlinks are safe
        candidate = candidate.resolve()

        if not candidate.is_file():
            return False

        mime, _ = mimetypes.guess_type(candidate.name)
        if not mime:
            # Fall through if the mimetype db failed to identify
            # basic web types
            ext = candidate.suffix
            # fallback to application/octet-stream if we really
            # have no idea
            mime = WEB_MIMETYPES.get(ext, "application/octet-stream")

        self.send_response(200)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(candidate.stat().st_size))
        self.end_headers()

        # Stream the file in chunks to avoid loading large files into memory
        with candidate.open("rb") as f:
            while True:
                data = f.read(8192)
                if not data:
                    break
                self.wfile.write(data)

        return True


def run(
    module_path: str | Path,
    host: str,
    port: int,
    livereload_port: int,
    livereload_host: str,
    force_polling: bool = False,
    extra_paths: list[str] | None = None,
):
    # Resolve to absolute before accessing parts to handle absolute file paths safely
    # If the user passed an absolute path, we inject its directory into sys.path
    mp_raw = Path(module_path)
    if mp_raw.is_absolute():
        if str(mp_raw.parent) not in sys.path:
            sys.path.insert(0, str(mp_raw.parent))
        mp = Path(mp_raw.name)
    else:
        mp = mp_raw

    if mp.suffix == ".py":
        mp = mp.with_suffix("")

    showcase_registry.clear()
    module_name = ".".join(mp.parts)

    if module_name in sys.modules:
        del sys.modules[module_name]

    importlib.invalidate_caches()

    app.Settings.livereload_host = livereload_host
    app.Settings.livereload_port = livereload_port

    try:
        module = importlib.import_module(module_name)
    except Exception as e:
        print(f"Error importing module {module_name}: {e}")
        raise
    assert module is not None

    watch_globs = []
    ignore_glob = []
    if extra_paths:
        for ep in extra_paths:
            watch_globs.append(ep)
    if hasattr(module, "__path__"):
        pathlist = module.__path__
    elif hasattr(module, "__file__"):
        pathlist = [os.path.dirname(cast(str, module.__file__))]
    else:
        pathlist = []
        print("Warning: could not determine module path for file watching")

    for watch_path in pathlist:
        loaded_mod_path = Path(watch_path)
        watch_globs.extend([f"{loaded_mod_path / '**/*.py'}"])
        ignore_glob.extend(
            [
                f"{loaded_mod_path / venv}"
                for venv in [
                    "venv",
                    ".venv",
                    ".virtualenv",
                    "virtualenv",
                    "env",
                    ".env",
                ]
            ]
        )
    fs_watcher = WatchCond(
        path_glob=watch_globs, ignore_glob=ignore_glob, action=None
    )

    watcher = Watcher([fs_watcher], force_polling=force_polling)

    def serve():
        server_address = (host, port)
        httpd = http.server.ThreadingHTTPServer(
            server_address, GalleryRequestHandler
        )
        print(f"Serving HTTP on http://{server_address[0]}:{server_address[1]}")
        httpd.serve_forever()

    server_thread = threading.Thread(target=serve, daemon=True)
    server_thread.start()
    livereload_thread = threading.Thread(
        target=livereload_server.live_reloader,
        args=(livereload_host, livereload_port),
        daemon=True,
    )
    livereload_thread.start()
    healthy = True
    backoff = 1.0
    last_error_str = None

    GalleryRequestHandler.content = show_showcases()
    changed_files = []
    while True:
        if healthy:
            while True:
                changed_files = watcher.changed()
                if changed_files:
                    print("Changes detected, reloading module...")
                    break
                sleep(0.1)
        else:
            # Poll for changes but with progressive sleep limit (backoff)
            waited = 0.0
            while waited < backoff:
                changed_files = watcher.changed()
                if changed_files:
                    break
                sleep(0.1)
                waited += 0.1

        if module_name in sys.modules:
            del sys.modules[module_name]

        importlib.invalidate_caches()

        try:
            showcase_registry.clear()
            env_registry.clear()
            module = importlib.import_module(module_name)
            GalleryRequestHandler.content.clear()
            GalleryRequestHandler.content.extend(show_showcases())
            healthy = True
            backoff = 1.0
            last_error_str = None

            if changed_files:
                livereload_server.reload_because(
                    [f.path for f in changed_files]
                )
        except Exception as e:
            healthy = False
            current_error_str = f"Error re-importing module {module_name}: {e}"
            if current_error_str != last_error_str:
                print(current_error_str)
                last_error_str = current_error_str
            backoff = min(backoff * 2, 10.0)
