from markupsafe import Markup, escape
from collections import deque
import typing
from dataclasses import MISSING
from typing import Iterable, Callable, TypeAlias


@typing.runtime_checkable
class _HasHtml(typing.Protocol):
    def __html__(self) -> str: ...


@typing.runtime_checkable
class ElementContext(typing.Protocol):
    def mask(self, BaseElement):
        pass

@typing.runtime_checkable
class _ContextAware(typing.Protocol):
    def context(self, ctx) -> str: ...


def escape_text(value) -> str:
    return escape(str(value))


def unsafe_text(value) -> str:
    return Markup(str(value))


ClassVariable: TypeAlias = (
    None | str | list[str] | dict[str, str] | dict[str, Callable] | list[Callable]
)


class BaseElement(_ContextAware):
    __slots__ = ("name", "_class", "_id", "_attrs", "_children", "_context")

    def __init__(
        self,
        name: str,
        Class: ClassVariable = None,
        id: str = None,
        children: list = None,
        **attrs,
    ) -> None:
        self.name = None
        if isinstance(Class, str):
            self._class = Class.split()
        elif isinstance(Class, list):
            self._class = Class
        elif isinstance(Class, dict):
            for key, value in Class.items():
                if value:  # filter hardcoded bools/nones out from the get go
                    self._class.append({key: value})

        self._class = Class
        self._id = id
        self._attrs = attrs
        if children is None:
            children = []
        self._children = children
        self._context = None

    def _convert_kwarg_attrs(self, attrs):
        if isinstance(attrs, dict):
            result = {}
            for key, value in attrs.items():
                if key == "_":
                    result[key] = value
                else:
                    result[key.replace("_", "-")] = value

        elif isinstance(attrs, list):
            return {attr: True for attr in attrs}
        

    def context(self, ctx):
        if self._context is None:
            self._context = deque()
        self._context.append(ctx)
        yield self
        self._context.remove(ctx)

    def _class_list_to_str(self, cls_list):
        """
        A class list supports the following formats:
        Class = ["btn", "btn-primary"]
        Class = [{"btn": True}, {"btn-primary": lambda x: True}]
        Class = ["btn", {"btn-primary": True}]
        Class = {"btn-primary": False}

        Convert all to a class string to be used in an element
        """
        cls_str = []
        for cls in cls_list:
            if callable(cls):
                cls_str.append(escape_text(cls()))
            elif isinstance(cls, str):
                cls_str.append(escape_text(cls))
            elif isinstance(cls, dict):
                for key, value in cls.items():
                    if not isinstance(key, str):
                        raise TypeError("Class key must be a string")

                    if callable(value):
                        result = value()
                        if result:
                            cls_str.append(escape_text(key))
                    elif value:
                        cls_str.append(escape_text(key))
            else:
                raise TypeError("Element class must be a string or callable")
        return " ".join(cls_str)

    def _attrs(self):
        """
        Build attr list to be inserted to html element

        """
        attrs = []
        cls_str = ""
        if self._class:
            cls_str = self._build_class_str(self._class)

        if "class" in self._attrs:
            if cls_str:
                cls_str = f"{cls_str} {self._build_class_str(self._attrs["class"])}"
            else:
                cls_str = self._build_class_str(self._attrs["class"])

        if cls_str:
            attrs.append(f'class="{cls_str}"')

        _id = self._id
        if "id" in self._attrs:
            # attr overrides self.id
            _id = self._attrs["id"]

        if _id:
            attrs.append(f'id="{escape_text(_id)}"')

        for key, value in self._attrs.items():
            if key in ('id', 'class'):
                continue
            
            if isinstance(value, bool):
                if value:
                    attrs.append(escape_text(key))
            else:
                if value is not None:
                    attrs.append(f'{escape_text(key)}="{escape_text(value)}"')
        return " ".join(attrs)

    def __getitem__(self, key):
        """
        Implements [] syntax which automatically appends to children list.

        Example:

        div()[
          "text",
          p()["text"],
          ul()[
            li["a"],
            li["b"]
          ]
        ]
        """
        # todo: consider raising based on type
        # todo: consider raising if chained:
        # div()[1,2][3]
        if isinstance(key, tuple):
            for k in key:
                self._children.append(k)

        return self

    def _materialize_child(item, context):
        if isinstance(item, str):
            return escape_text(item)
        elif isinstance(item, _HasHtml):
            return item.__html__()

    def __iter__(self) -> typing.Iterator[str]:
        yield f"{self.name}{' '.join(self._class)}"
        pass

    def __html__(self):
        pass

    # def __str__(self) -> _Markup:
    # return _Markup("".join(self))


Node: TypeAlias = (
    None
    | bool
    | str
    | int
    | BaseElement
    | _HasHtml
    | Iterable["Node"]
    | Callable[[], "Node"]
    | _ContextAware
)


class img(BaseElement):
    def __init__(
        self,
        Class: str = None,
        id: str = None,
        src: str = None,
        alt: str = None,
        **attrs,
    ) -> None:
        super().__init__("img", Class, id, src=src, alt=alt, **attrs)


def iter_children(element, ctx) -> typing.Iterable:
    # If this element is a function, call it until it resolves
    while not isinstance(element, BaseElement) and callable(element):
        if isinstance(element, _ContextAware):
            with element.context(ctx) as x:
                element = x()
        else:
            element = element()

    if element is None:
        return

    if element in (True, False):
        # No bools
        return

    if isinstance(element, BaseElement):
        if element._children is None:
            return None
        with element.context(ctx):
            for child in element._children:
                yield from iter_children(child, ctx)
    elif isinstance(element, str):
        yield escape_text(element)
    elif isinstance(element, int):
        yield str(element)
    elif isinstance(element, _HasHtml):
        yield unsafe_text(element.__html__())
