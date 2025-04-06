from typing import Optional, Union

from . import base_types, doctype, pretty_print, unsafe_text
from . import elements as el
from .util_funcs import get_livereload_env


def HTML5Document(
    title: Optional[str] = None,
    lang: Optional[str] = None,
    head: Optional[list] = None,
    body: Union[list[base_types.Node], el.body, None] = None,
    prettify: Union[bool, str] = False,
) -> str:
    """
    Return an HTML5 document with the given title and content.
    It also defines meta viewport for mobile support.

    When using livereload, an environment variable is set which adds
    livereload-js to the head of the document.

    :param title: The title of the document
    :param lang: The language of the document.
                 English is "en", or consult HTML documentation
    :param head: Children to add to the <head> element,
                 which already defines viewport and title
    :param body: A 'body' element or a list of children to add to the 'body' element
    :param prettify: If true, prettify HTML output.
                     If the value is a string, use that parser for BeautifulSoup
    """
    # Enable HTML5 and prevent quirks mode
    header = doctype("html")

    head_el = el.head()[
        el.meta(  # enable mobile rendering
            name="viewport", content="width=device-width, initial-scale=1.0"
        ),
        el.title()[title] if title else None,
        head if head else None,
    ]
    # None if disabled
    live_reload_flags = get_livereload_env()
    # Feature: Live reloading for development
    # Fires when HTMLCOMPOSE_LIVERELOAD=1
    if live_reload_flags:
        head_el.append(_livereload_script_tag(live_reload_flags))

    if isinstance(body, el.body):
        body_el = body
    else:
        body_el = el.body()[body]
    html = el.html(lang=lang)[head_el, body_el]
    result = f"{header}\n{html.render()}"
    if prettify:
        return pretty_print(result)
    else:
        return result


def get_livereload_uri() -> str:
    """
    Generally this is just the neat place to store the livereload URI.

    But if the user wants they can override this function to return a local
    resource i.e.

    html_compose.document.get_live_reload_uri =
      lambda: "mydomain.com/static/livereload.js";

    """
    VERSION = "v4.0.2"
    return f"cdn.jsdelivr.net/npm/livereload-js@{VERSION}/dist/livereload.js"


def _livereload_script_tag(live_reload_settings):
    """
    Returns a script tag which injects livereload.js.
    """
    # Fires when HTMLCOMPOSE_LIVERELOAD=1
    # Livereload: https://github.com/livereload/livereload-js
    uri = get_livereload_uri()

    proxy_uri = live_reload_settings["proxy_uri"]
    proxy_host = live_reload_settings["proxy_host"]
    if proxy_host:
        # Websocket is behind a proxy, likely SSL
        # Port isn't important for these but the URI is
        if proxy_uri.startswith("/"):
            proxy_uri = proxy_uri.lstrip("/")
        uri_encoded_flags = f"host={proxy_host}&path={proxy_uri}"
    else:
        # Regular development enviroment with no proxy. host:port will do.
        host = live_reload_settings["host"]
        port = live_reload_settings["port"]
        uri_encoded_flags = f"host={host}&port={port}"

    # This scriptlet auto-inserts the livereload script and detects protocol
    return el.script()[
        unsafe_text(
            "\n".join(
                [
                    "(function(){",
                    'var s = document.createElement("script");',
                    f"s.src = location.protocol + '//{uri}?{uri_encoded_flags}';",
                    "document.head.appendChild(s)",
                    "})()",
                ]
            )
        )
    ]
