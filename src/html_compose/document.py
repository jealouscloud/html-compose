from typing import Optional, Union

from . import base_types, doctype, pretty_print
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
        # Add livereload script to the head
        # Livereload: https://github.com/livereload/livereload-js
        # We pin version and used an SRI hash generator to prevent supply-chain attacks
        # https://www.srihash.org/
        VERSION = "v4.0.2"
        uri = f"https://cdn.jsdelivr.net/npm/livereload-js@{VERSION}/dist/livereload.min.js"
        head_el.append(
            el.script(
                {
                    "src": f"{uri}?{live_reload_flags}",
                    "integrity": "sha384-JpRTIH2FPXE1xxxYlwSn2HF2U5br0oTSUBvdF0F5YcNmUTvJvh/o1+rDUdy9NGVs",
                    "crossorigin": "anonymous",
                }
            )
        )
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
