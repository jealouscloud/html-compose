from typing import Any, Generator, Iterable, Literal, TypeAlias
from urllib.parse import urlencode

from . import base_types, doctype, pretty_print, resource, unsafe_text
from . import elements as el
from .util_funcs import get_livereload_env

Node: TypeAlias = base_types.Node


def generate_head(
    title: str | None = None,
    js: Iterable[str | resource.js_import] | None = None,
    css: Iterable[str | resource.css_import] | None = None,
    fonts: Iterable[resource.font_import_manual | resource.font_import_provider]
    | None = None,
    extra: Iterable[Node] | None = None,
    skip_meta: bool = False,
) -> el.head:
    """
    Generate a head element with common imports and arguments.

    By default, this includes a viewport meta tag.

    :param title: HTML document title
    :param js: A list of javascript imports to include in the head
    :param css: A list of CSS imports to include in the head
    :param fonts: A list of font imports to include in the head
    :param extra: Any extra elements to include at the end of the head
    :param skip_meta: Skip the meta viewport tag

    :return: A head element with the specified imports and title
    """
    head_elements: list[Node] = resource.to_elements(
        js=js, css=css, fonts=fonts
    )
    if extra:
        head_elements.extend(extra)

    return el.head()[
        el.meta(
            name="viewport", content="width=device-width, initial-scale=1.0"
        )
        if not skip_meta
        else None,
        el.title()[title] if title else None,
        head_elements,
    ]


def document_streamer(
    lang: str | None = None,
    head: Iterable[Node] | el.head | None = None,
    body: Iterable[Node] | el.body | None = None,
    stream_mode: Literal["head_only", "full"] = "head_only",
) -> Generator[str, Any, None]:
    """
    Return a full HTML5 document as a generator, yielding parts as strings.

    stream_mode controls whether to yield just the head first, then body,
    or the full document in parts.

    tldr:
    ```
      doctype("html")
      html(lang=lang)[
        head[
          meta(name="viewport", content="width=device-width, initial-scale=1.0")
          ...,
        ]
        body[body]]
    ```

    When using livereload, an environment variable is set which adds
    livereload-js to the head of the document.

    :param lang: The language of the document.
                 English is "en", or consult HTML documentation
    :param head: Children to add to the <head> element,
                 which already defines viewport.
                 A head element passed directly will be used unmodified.
    :param body: A 'body' element or a list of children to add to the 'body' element
    :param stream_mode: If set, return a generator that yields parts of the document.
                        "head_only" yields the head, then full body,
                        "full" yields the entire document in parts.

    :return: A generator that yields parts of the HTML5 document as strings
    """
    # Enable HTML5 and prevent quirks mode
    header = doctype("html")
    if isinstance(head, el.head):
        head_el = head
    else:
        head_el = generate_head(extra=head)
    # None if disabled
    live_reload_flags = get_livereload_env()
    # Feature: Live reloading for development
    # Fires when HTMLCOMPOSE_LIVERELOAD=1
    if live_reload_flags:
        head_el.append(_livereload_script_tag(live_reload_flags))
    # Produce our HTML element and save its parts
    html_el = el.html(lang=lang).resolve()
    html_el_start = next(html_el)
    html_el_end = next(html_el)
    # Yield up until end of the head element
    yield f"{header}\n{html_el_start}\n{head_el.render()}\n\n"

    # Setup the body element
    if isinstance(body, el.body):
        body_el = body
    else:
        body_el = el.body()[body]
    if stream_mode == "full":
        # Resolve in pieces
        for body_part in body_el.resolve():
            yield body_part
        yield "\n"
        yield html_el_end
    elif stream_mode == "head_only":
        # Resolve all at once
        yield f"{body_el.render()}\n{html_el_end}"
    else:
        raise ValueError("stream_mode must be 'head_only' or 'full'")


def document_generator(
    lang: str | None = None,
    head: el.head | list | None = None,
    body: Iterable[Node] | el.body | None = None,
) -> str:
    """
    Return a full HTML5 document as a string.

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


    :param lang: The language of the document.
                 English is "en", or consult HTML documentation
    :param head: Children to add to the <head> element,
                 which already defines viewport.
                 A head element passed directly will be used unmodified.
    :param body: A 'body' element or a list of children to add to the 'body' element

    :return: A full HTML5 document as a string

    """
    return "".join(
        document_streamer(lang=lang, head=head, body=body, stream_mode="full")
    )


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


class HTML5Document:
    """
    A convenience class to generate a full HTML5 document.

    Allows you to specify common elements like JavaScript and CSS imports,
    as well as additional head content.

    When using livereload, an environment variable is set which adds
    livereload-js to the head of the document.
    """

    def __init__(
        self,
        title: str | None = None,
        lang: str | None = None,
        js: Iterable[str | resource.js_import] | None = None,
        css: Iterable[str | resource.css_import] | None = None,
        fonts: Iterable[
            resource.font_import_manual | resource.font_import_provider
        ]
        | None = None,
        head_extra: Iterable[Node] | None = None,
        body: Iterable[Node] | el.body | None = None,
    ) -> None:
        """

        :param title: The title of the document
        :param lang: The language of the document.
                     English is "en", or consult HTML documentation
        :param js: A list of javascript imports to include in the head
        :param css: A list of CSS imports to include in the head
        :param fonts: A list of font imports to include in the head
        :param head_extra: Additional elements to include in the head
        :param body: A 'body' element or a list of elements to include in the body
        :param stream_mode: If set, return a generator that yields parts of the document.
                            "head_only" yields the head, then full body,
                            "full" yields the entire document in parts.
        """
        self.title = title
        self.lang = lang
        self.js = js
        self.css = css
        self.fonts = fonts
        self.head_extra = head_extra
        if isinstance(body, el.body):
            self.body = body
        else:
            self.body = el.body()[body]

    def render(self) -> str:
        """
        Return the full HTML5 document as a string.
        """
        return "".join(self.stream(stream_mode="full"))

    def stream(
        self, stream_mode: Literal["head_only", "full"] = "head_only"
    ) -> Generator[str, Any, None]:
        """
        Return a generator that yields parts of the HTML5 document as strings.

        :param stream_mode: Parts of the document to stream. If "head_only",
                            we yield the head, then the full body.
                            If "full", we yield the entire document in parts.

        :return: A generator that yields parts of the HTML5 document as strings.
        """
        return document_streamer(
            lang=self.lang,
            head=generate_head(
                title=self.title,
                js=self.js,
                css=self.css,
                fonts=self.fonts,
                extra=self.head_extra,
            ),
            body=self.body,
            stream_mode=stream_mode,
        )

    def __html__(self) -> str:
        return self.render()

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return pretty_print(str(self))
