import json
import threading
from time import sleep
from typing import Optional

from websockets.sync.server import Server, serve

sockets = set()
server: Optional[Server] = None


def run_ws(websocket):
    """
    Run livereload-js websocket server.
    ref: https://web.archive.org/web/20180208220539/http://livereload.com/api/protocol/
    """
    sockets.add(websocket)
    try:
        for message in websocket:
            msg = json.loads(message)
            command = msg["command"]
            # Each client MUST be greeted with a hello
            if command == "hello":
                protocols = msg["protocols"]
                our_protocol = "http://livereload.com/protocols/official-7"

                assert our_protocol in protocols, "Expected protocol not found"

                websocket.send(
                    json.dumps(
                        {"command": "hello", "protocols": [our_protocol]}
                    )
                )
            # We ignore all other commands for now
    finally:
        sockets.remove(websocket)


def reload_because(paths: list[str]) -> None:
    """
    Trigger a livereload in the browser
    Provide list of paths to livereload-js
    Not really sure why we're sending paths, but that's how it's done in livereload-js
    """
    for socket in sockets:
        for path in paths:
            socket.send(json.dumps({"command": "reload", "path": path}))


def live_reloader(host, port):
    with serve(run_ws, host, port) as srv:
        global server
        server = srv
        server.serve_forever()


def close():
    if server:
        server.shutdown()


def run_server(host, port) -> Server:
    print(f"Starting livereload WebSocket server at ws://{host}:{port}")
    threading.Thread(
        target=live_reloader, args=(host, port), daemon=True
    ).start()
    global server
    while server is None:
        sleep(0.25)
    return server
