from markupsafe import Markup, escape
from typing import Union


def escape_text(value) -> Markup:
    """
    Escape unsafe text to be inserted to HTML

    Optionally casting to string
    """
    if isinstance(value, str):
        return escape(value)
    else:
        return escape(str(value))


def unsafe_text(value: Union[str, Markup]) -> Markup:
    """
    Return input string as Markup

    If input is already markup, it needs no further casting
    """
    if isinstance(value, Markup):
        return value

    return Markup(str(value))
