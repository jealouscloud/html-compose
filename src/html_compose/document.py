from typing import Optional, Union

from . import base_types, doctype
from . import elements as el


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
    if isinstance(body, el.body):
        body_el = body
    else:
        body_el = el.body()[body]
    html = el.html(lang=lang)[
        head_el,
        body_el,
    ]
    result = f"{header}\n{html.render()}"
    if prettify:
        from bs4 import BeautifulSoup

        return BeautifulSoup(
            result, features="html.parser" if prettify is True else prettify
        ).prettify()
    else:
        return result
