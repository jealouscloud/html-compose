# Idea
If it takes multiple steps to make a change, I'm going to make a change slowly.

If I have to do nothing to notice my change immediately, I'm going to make changes quickly.

The idea is to iterate rapidly, so we provide a generic tool to help you do just that.

## Live Reload
Live reload is an optional feature of html-compose to aid in rapid development.

Browser based livereload is provided by 
[livereload-js](https://www.npmjs.com/package/livereload-js). 

To trigger it, we host a websocket server on port 51353 by default.

Our library comes optionally equipped with a file watcher that derives certain actions from
file events.

It can be used to run your webserver and build commands in certain events.
## Path expressions
Paths expressions essentially globs as you understand them from `glob.glob`
with recursive=True.

Ignore_glob and path_glob use the same mechanism.

### Regular glob
They support regular file globbing where * is 1 or more characters i.e. `*.py`

### Recursive glob
They support recursion via `**` which matches any 0 or more directories:  
`src/**/*.py` will match both `src/demo.py` and `src/my/nested/dir/demo.py`.

### Trailing / (recursive)
A trailing `/` will also be interpreted as a recursive match i.e.

`src/` will match `src/any/file.txt`
## Example usage
This demonstrates a Flask application uses a combination of vanilla js and bundled node dependencies.

`live.py`
```python
import html_compose.live as live

live.server(
    daemon=live.ShellCommand(
        "flask --app ./src/web_demo/server.py run"
    ),
    daemon_delay=1,
    # These conditions determine when to reload the flask app
    # And commands to run based on the matching condition
    conds=[
        live.WatchCond(
            # Trigger reload when a python file changes
            path_glob="src/**/*.py",
            ignore_glob="src/.venv/"
            action=None,
        ),
        live.WatchCond(
            "node-app/**/*.js",
            action=live.ShellCommand("./build.sh"),
            # no_reload means not to try to reload the daemon
            no_reload=True,
        ),
        live.WatchCond(
            # Trigger reload when the bro
            "public/**/*.js",
            action=None,
        ),
    ],
    host="localhost",
    port=51353,
)
```
`build.sh`
```shell
#!/usr/bin/env bash
(cd node-app && (
    ./node_modules/.bin/esbuild ./myapp.js --bundle --outfile=../public/node-app.js
  )
)
```

running: 
```
[~/src/mine/web-demo]$ python3 livereload.py 
Monitoring for changes: src
Monitoring for changes: node-app
Monitoring for changes: public
Monitoring 3 path(s) via RustNotify. 3 path(s) are monitored recursively.
Starting livereload WebSocket server at ws://localhost:51353
 * Serving Flask app './src/web_demo/server.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
Changed: node-app/myapp.js

  ../public/node-app.js  316.6kb

⚡ Done in 16ms
Changed: public/node-app.js
Reloading daemon after 1.0 seconds...
 * Serving Flask app './src/web_demo/server.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

## TLS
Live reload is a development feature and not recommended for production.

However there are some instances in which you can only debug behind a TLS server.

To prevent mixed content errors, livereload auto-detects the protocol from the URI. However, we do not ship settings for configuring TLS.

In order to make TLS work, serve the websocket behind a reverse proxy.

If you're using nginx, you would include something like this in your server block:
```
    location /ws/ {
        proxy_pass http://localhost:51353;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_set_header Host $host;
    }
```

Since you're serving your websocket over SSL, you can now specify when calling `live.server(`:
* `proxy_host`: host to reach for the livereload websocket. used in browser instead of `host` parameter.

    Example: `my-sweet-website.com`
* `proxy_uri`: URI

    Example: `/ws/`