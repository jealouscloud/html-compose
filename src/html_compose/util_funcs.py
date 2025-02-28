import inspect
from functools import lru_cache
from typing import Any, Generator, Iterable

from bs4 import BeautifulSoup  # type: ignore[import-untyped]


def pretty_print(html: str) -> str:
    p = BeautifulSoup(html, features="html.parser")
    return p.prettify()


def join_attrs(k, value_trusted):
    """
    Join escaped value to key in form key="value"
    """
    return f'{k}="{value_trusted}"'


def is_iterable_but_not_str(input_iterable):
    """
    Check if an iterable is not a string or bytes.
    Which prevents some bugs.
    """
    return isinstance(input_iterable, Iterable) and not isinstance(
        input_iterable, (str, bytes)
    )


def flatten_iterable(input_iterable: Iterable) -> Generator[Any, None, None]:
    """
    Flatten an iterable of iterables into a single iterable
    """
    stack = [iter(input_iterable)]

    while stack:
        try:
            # Get next element from top iterator on the stack
            current = next(stack[-1])
            if is_iterable_but_not_str(current):
                stack.append(
                    iter(current)
                )  # Push new iterator for the current iterable item
            else:
                # Item isn't iterator, yield it.
                yield current
        except StopIteration:
            # The iterator was exhausted
            stack.pop()


@lru_cache(maxsize=500)
def get_param_count(func):
    return len(inspect.signature(func).parameters)


def safe_name(name):
    """
    Some names are reserved in Python, so we need to add an underscore
    An underscore after was chosen so type hints match what user is looking for
    """
    # Keywords
    if name in ("class", "is", "for", "as", "async", "del"):
        name = name + "_"

    if "-" in name:
        # Fixes for 'accept-charset' etc.
        name = name.replace("-", "_")

    return name
