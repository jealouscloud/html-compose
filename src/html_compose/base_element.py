from typing import Any, Callable, Generator, Optional, Union

from . import escape_text, unsafe_text, util_funcs
from .attributes import BaseAttribute, GlobalAttrs
from .base_types import (
    ElementBase,
    Node,
    _HasHtml,
)

SPECIAL_ATTRS = {
    "class": GlobalAttrs.class_,
    "style": GlobalAttrs.style,
}


class BaseElement(ElementBase, GlobalAttrs):
    """
    Base HTML element

    All elements derive from this class
    """

    __slots__ = ("name", "_attrs", "_children", "data")

    def __init__(
        self,
        name: str,
        void_element: bool = False,
        id: Union[str, GlobalAttrs.id] = None,
        class_: Union[str, GlobalAttrs.class_] = None,
        attrs: Union[dict[str, str], list[BaseAttribute]] = None,
        data: Optional[Any] = None,
        children: list = None,
    ) -> None:
        """
        Initialize an HTML element

        Args:
            name (str): The name of the element.
            void_element (bool): Indicates if the element is a void element. Defaults to False.
            id (str): The ID of the element. Defaults to None.
            class_: The class of the element. Defaults to None.
            attrs: A list of attributes for the element.
                It can also be a dictionary of key,value strings.
                Defaults to None.
            data: Non-rendered user data for the element. Defaults to None.
            children: A list of child elements. Defaults to None.
        """
        self.name = name
        if attrs is None:
            attrs = []

        self._attrs = self._resolve_attrs(attrs)

        self._process_attr("id", id)
        self._process_attr("class", class_)

        self._children = children
        self.data = data
        self.is_void_element = void_element

    def _process_attr(self, attr_name, attr_data):
        if attr_data is None or attr_data is False:
            return  # noop

        if not isinstance(attr_data, BaseAttribute):
            attr_class = SPECIAL_ATTRS.get(attr_name, BaseAttribute)
            attr = attr_class(attr_data)

        result = attr.evaluate()
        if result is not None:
            _, resolved_value = result
            if attr_name in self._attrs:
                if attr_name == "class":
                    self._attrs[attr_name] = (
                        f"{resolved_value} {self._attrs[attr_name]}"
                    )
                elif attr_name == "style":
                    self._attrs[attr_name] = (
                        f"{resolved_value}; {self._attrs[attr_name]}"
                    )
                else:
                    raise ValueError(
                        f"Attribute {attr_name} waas passed twice. "
                        "We don't know how to merge it."
                    )
            else:
                self._attrs[attr_name] = resolved_value

    def append(self, *child_or_childs: Node):
        if self.is_void_element:
            raise ValueError(f"Void element {self.name} cannot have children")

        args = child_or_childs
        # Special case: We may have been passed a literal tuple
        # If it has one child that itself is a tuple, unbox it.
        if (
            isinstance(args, tuple)
            and len(args) == 1
            and isinstance(args[0], tuple)
        ):
            args = args[0]

        # Unbox any literal tuple, lists
        if isinstance(args, tuple) or isinstance(args, list):
            for k in args:
                self._children.append(k)
        else:
            # Let the child resolver step handle it
            # Applies to iterables, callables, literal elements
            self._children.append(args)

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
        self.append(key)

        return self

    def _call_callable(self, func, parent):
        """
        Executor for callable elements

        These elements may accept 0-2 positional args:
        0: None
        1: self (The function may consider it "parent")
        2: the parents parent

        """
        param_count = util_funcs.get_param_count(func)

        assert param_count in range(0, 3), (
            "Element resolution expects 0 - 2 parameter callables"
            f", got {param_count} params"
        )

        if param_count == 0:
            result = func()
        elif param_count == 1:
            result = func(self)
        elif param_count == 2:
            result = func(self, parent)

        return result

    def resolve_child(
        self, child: Node, call_callables, parent
    ) -> Generator[str, None, None]:
        """
        Child resolver for elements

        Returns raw HTML string for child

        If call_callables is false, callables are yielded.
        """

        if child is None:
            # null child, possibly from the callable.
            # Magic: We ignore null children for things like
            # div[
            #   button if needs_button else None
            # ]
            yield from ()

        elif isinstance(child, str):
            yield escape_text(child)

        elif isinstance(child, int):
            # escape_text will str()
            yield escape_text(child)

        elif isinstance(child, float):
            # Magic: Convert float to string with fixed ndigits
            # This avoids weird output like 6.33333333333...
            yield escape_text(round(child, self.__class__.FLOAT_PRECISION))

        elif isinstance(child, bool):
            # Magic: Convert to 'typical' true/false
            # Most people using this would be better using None
            # which specifically means "no render"
            # But some weirdos may be trying to render true/false literally
            yield unsafe_text("true" if child else "false")

        elif isinstance(child, ElementBase):
            child: ElementBase
            # Recursively resolve the element tree
            yield from child.resolve(self)

        elif isinstance(child, _HasHtml):
            # Fetch raw HTML from object
            yield unsafe_text(child.__html__())

        elif util_funcs.is_iterable_but_not_str(child):
            for el in util_funcs.flatten_iterable(child):
                yield from self.resolve_child(el, call_callables, parent)

        elif callable(child):
            if not call_callables:
                # In deferred resolve state,
                # callables are yielded instead of resolved
                yield child
            else:
                result = child
                while callable(result):
                    result = self._call_callable(child, parent)

                yield from self.resolve_child(result, call_callables, parent)
        else:
            raise ValueError(f"Unknown child type: {type(child)}")

    def resolve_tree(
        self, parent=None
    ) -> Generator[Union[str, Callable], None, None]:
        """
        Walk html element tree and yield all resolved children

        Callables are yielded instead of resolved

        Return:
            escaped (trusted) HTML strings
        """

        for child in self._children:
            child: Node
            yield from self.resolve_child(
                child, call_callables=False, parent=parent
            )

    def _resolve_attrs(self, attrs) -> dict[str]:
        """
        Resolve attributes into key/value pairs
        """
        if not attrs:
            return {}

        attr_dict = {}
        # These are sent to us in format:
        # key, value (unescaped)
        if isinstance(attrs, (list, tuple)):
            for item in attrs:
                if isinstance(item, BaseAttribute):
                    result = item.evaluate()
                    if not result:
                        continue
                    key, value = result
                    attr_dict[key] = value
                elif isinstance(item, tuple) and len(item) == 2:
                    attr = BaseAttribute(item[0], item[1]).evaluate()
                    if not attr:
                        continue

                    a_name, a_value = attr
                    attr_dict[a_name] = a_value
                elif isinstance(item, dict):
                    for key, value in item.items():
                        attr = BaseAttribute(key, value).evaluate()
                        if not attr:
                            continue
                        a_name, a_value = attr
                        attr_dict[a_name] = a_value
                else:
                    raise ValueError(
                        f"Unknown type for attr value: {type(item)}."
                    )

        elif isinstance(attrs, dict):
            for key, value in attrs.items():
                attr = BaseAttribute(key, value).evaluate()
                if attr:
                    a_name, a_value = attr
                    attr_dict[a_name] = a_value

            attr_dict = attrs
        else:
            raise ValueError(f"Unknown: {type(attrs)}")

        return attr_dict

    def deferred_resolve(self, parent) -> Generator[str, None, None]:
        """
        Resolve all attributes and children of the HTML element, except for callable children.

        This method performs the following steps:
        1. Resolves all attributes of the element.
        2. Resolves all non-callable children.
        3. Applies context hooks if applicable.
        4. Generates the HTML string representation of the element.

        Returns:
            Generator[str, None, None]: A generator that yields strings representing
            parts of the HTML element. These parts include:
            - The opening tag with attributes
            - The content (children) of the element
            - The closing tag

        Note:
            - For void elements, only the self-closing tag is yielded.
            - Callable children are not resolved in this method.
        """

        # attrs is a defaultdict of strings.
        # The key is the attr name, the value is the attr value unescaped.
        attrs = self._attrs

        children = None

        if not self.is_void_element:
            children = [child for child in self.resolve_tree()]

        # join_attrs has a configurable lru_cache
        join_attrs = self.get_attr_join()

        # Generate the key="value" pairs for the attributes
        # The value escape step lives here because we trust no
        # previous step in the pipeline.
        attr_string = " ".join(
            (join_attrs(k, escape_text(v)) for k, v in attrs.items())
        )

        if self.is_void_element:
            yield f"<{self.name} {attr_string}/>"
        else:
            if attr_string:
                yield f"<{self.name} {attr_string}>"
            else:
                yield f"<{self.name}>"

            yield from children
            yield f"</{self.name}>"

    def resolve(self, parent=None) -> Generator[str, None, None]:
        """
        Generate the flat HTML [string] iterator for the HTML element
        """
        resolver = self.deferred_resolve(parent)
        for element in resolver:
            if callable(element):
                # Feature: nested calling similar to a functional programming style
                yield from self.resolve_child(
                    element, call_callables=True, parent=parent
                )
            else:
                yield element

    def render(self, parent=None) -> str:
        """
        Render the HTML element
        """
        return "".join(self.resolve(parent))

    def __str__(self) -> str:
        return self.__html__()

    def __html__(self):
        """
        Render the HTML element
        """
        return self.render()
