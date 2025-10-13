from typing import Any, Generator, Iterable, Literal
from urllib.parse import urlencode

from . import base_types, doctype, pretty_print, resource, unsafe_text
from . import elements as el
from .util_funcs import get_livereload_env


def document_streamer(
    title: str | None = None,
    lang: str | None = None,
    js: Iterable[str | resource.js_import] | None = None,
    css: Iterable[str | resource.css_import] | None = None,
    fonts: Iterable[resource.font_import_manual | resource.font_import_provider]
    | None = None,
    head_extra: Iterable[base_types.Node] | None = None,
    body_content: Iterable[base_types.Node] | el.body | None = None,
    stream_mode: Literal["head_only", "full"] = "head_only",
) -> Generator[str, Any, None]:
    """
    A convenience function to generate a full HTML5 document.

    This is a higher-level function that wraps around HTML5Document,
    allowing you to specify common elements like JavaScript and CSS imports,
    as well as additional head content.

    :param title: The title of the document
    :param lang: The language of the document.
                 English is "en", or consult HTML documentation
    :param js: A list of javascript imports to include in the head
    :param css: A list of CSS imports to include in the head
    :param head_extra: Additional elements to include in the head
    :param body_content: A 'body' element or a list of children to add to the 'body' element
    :param stream_mode: If set, return a generator that yields parts of the document.
                        "head_only" yields the head, then full body,
                        "full" yields the entire document in parts.
    :return: A complete HTML5 document as a string generator
    """
    head_elements: list[base_types.Node] = resource.to_elements(js, css, fonts)
    if head_extra:
        head_elements.extend(head_extra)
    return HTML5Stream(
        title=title,
        lang=lang,
        head=head_elements,
        body=body_content,
        stream_mode=stream_mode,
    )


def document_generator(
    title: str | None = None,
    lang: str | None = None,
    js: Iterable[str | resource.js_import] | None = None,
    css: Iterable[str | resource.css_import] | None = None,
    fonts: Iterable[resource.font_import_manual | resource.font_import_provider]
    | None = None,
    head_extra: Iterable[base_types.Node] | None = None,
    body_content: Iterable[base_types.Node] | el.body | None = None,
) -> str:
    """
    A convenience function to generate a full HTML5 document.

    This is a higher-level function that wraps around HTML5Document,
    allowing you to specify common elements like JavaScript and CSS imports,
    as well as additional head content.

    :param title: The title of the document
    :param lang: The language of the document.
                 English is "en", or consult HTML documentation
    :param js: A list of javascript imports to include in the head
    :param css: A list of CSS imports to include in the head
    :param head_extra: Additional elements to include in the head
    :param body_content: A 'body' element or a list of children to add to the 'body' element
    :return: A complete HTML5 document as a string
    """
    return "".join(
        document_streamer(
            title=title,
            lang=lang,
            js=js,
            css=css,
            fonts=fonts,
            head_extra=head_extra,
            body_content=body_content,
            stream_mode="full",
        )
    )


def HTML5Stream(
    title: str | None = None,
    lang: str | None = None,
    head: list | None = None,
    body: Iterable[base_types.Node] | el.body | None = None,
    stream_mode: Literal["head_only", "full"] = "head_only",
) -> Generator[str, Any, None]:
    """
    A streaming version of HTML5Document.

    tldr:
    ```
      doctype("html")
      html(lang=lang)[
        head[
          meta(name="viewport", content="width=device-width, initial-scale=1.0")
          title(title)
        ]
        body[body]]
    ```

    When using livereload, an environment variable is set which adds
    livereload-js to the head of the document.

    :param title: The title of the document
    :param lang: The language of the document.
                 English is "en", or consult HTML documentation
    :param head: Children to add to the <head> element,
                 which already defines viewport and title
    :param body: A 'body' element or a list of children to add to the 'body' element
    :param stream_mode: If set, return a generator that yields parts of the document.
                        "head_only" yields the head, then full body,
                        "full" yields the entire document in parts.

    :return: A generator that yields parts of the HTML5 document as strings
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
    html_el = el.html(lang=lang).resolve()
    html_el_start = next(html_el)
    html_el_end = next(html_el)
    yield f"{header}\n{html_el_start}\n{head_el.render()}\n\n"
    if isinstance(body, el.body):
        body_el = body
    else:
        body_el = el.body()[body]
    if stream_mode == "full":
        for body_part in body_el.resolve():
            yield body_part
        yield "\n"
        yield html_el_end
    elif stream_mode == "head_only":
        yield f"{body_el.render()}\n{html_el_end}"
    else:
        raise ValueError("stream_mode must be 'head_only' or 'full'")


def HTML5Document(
    title: str | None = None,
    lang: str | None = None,
    head: list | None = None,
    body: Iterable[base_types.Node] | el.body | None = None,
    prettify: bool | str = False,
) -> str:
    """
    Return an HTML5 document with the given title and content.
    It also defines meta viewport for mobile support.

    tldr:
    ```
      doctype("html")
      html(lang=lang)[
        head[
          meta(name="viewport", content="width=device-width, initial-scale=1.0")
          title(title)
        ]
        body[body]]
    ```

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
    result = "".join(
        HTML5Stream(
            title=title, lang=lang, head=head, body=body, stream_mode="full"
        )
    )
    if prettify:
        if prettify is True:
            return pretty_print(result)
        return pretty_print(result, features=prettify)
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
        uri_encoded_flags = urlencode({"host": proxy_host, "path": proxy_uri})
    else:
        # Regular development enviroment with no proxy. host:port will do.
        host = live_reload_settings["host"]
        port = live_reload_settings["port"]
        uri_encoded_flags = urlencode({"host": host, "port": port})

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
