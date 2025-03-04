import typing
from functools import lru_cache
from typing import Callable, Iterable

from . import util_funcs


@typing.runtime_checkable
class _HasHtml(typing.Protocol):
    def __html__(self) -> str:
        """
        Return unsafe HTML string
        """
        ...


class ElementBase(_HasHtml):
    """
    Base class for all HTML elements

    Defined here to avoid circular imports for Node definition

    Implementers define: __init__, render, context, __html__

    See: BaseElement
    """

    FLOAT_PRECISION = 3  # Used when marshalling child floats into strings
    ATTR_CACHE_SIZE = (
        250  # Number of translated attributes to cache strings for
    )

    def __init__(self):
        raise NotImplementedError

    def get_attr_join(self) -> Callable[[str, str], str]:
        """
        Return join_attrs(key: str, value_trusted: str) function with lru cache
        The returned function turns key, value into key="value"
        """
        cls = self.__class__

        if hasattr(cls, "_join_lru_maxsize"):
            live_size = cls._join_lru_maxsize  # pyright: ignore[reportAttributeAccessIssue]
        else:
            cls._join_lru_maxsize = cls.ATTR_CACHE_SIZE  # type: ignore[attr-defined]
            live_size = None

        if live_size != cls.ATTR_CACHE_SIZE:
            cls.join_attrs = lru_cache(maxsize=cls.ATTR_CACHE_SIZE)(  # type: ignore[attr-defined]
                util_funcs.join_attrs
            )

        return cls.join_attrs  # type: ignore[attr-defined]

    def render(self, parent=None) -> str:
        return "".join(self.resolve(parent))

    def resolve(self, parent=None) -> Iterable[str]:
        """
        Yield all html as a generator of strings
        """
        raise NotImplementedError()

    def __html__(self) -> str:
        return self.render()


# The Node type is a union of all possible types that can be rendered
Node = (
    None  # None will not be appended to the output children
    | str  # Text that needs to be escaped
    | int  # Integer that needs to be converted to str
    | float  # Float that needs to be converted to str
    | bool  # Boolean that needs to be converted to str - usually a mistake
    | ElementBase  # Base class for all HTML elements
    | _HasHtml  # Returns HTML that does not need escaping
    | Iterable["Node"]
    | Callable[[], "Node"]
)
