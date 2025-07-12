from typing import Callable, Generator, Optional, Union

from . import escape_text, unsafe_text, util_funcs
from .attributes import BaseAttribute, GlobalAttrs
from .base_types import ElementBase, Node, _HasHtml

SPECIAL_ATTRS = {"class": GlobalAttrs.class_, "style": GlobalAttrs.style}


class BaseElement(ElementBase):
    """
    Base HTML element

    All elements derive from this class
    """

    __slots__ = ("tag", "attrs", "_children", "is_void_element")

    @classmethod
    def __class_getitem__(cls, key):
        """
        This implements a shortcut to the constructor for a given element.

        Example:
        If the user passes `h1["Demo"]` the user likely expects h1()["Demo"]
        """
        return cls()[key]  # pyright: ignore[reportCallIssue]

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

    def __init__(
        self,
        tag: str,
        void_element: bool = False,
        attrs: Union[
            dict[str, Union[str, list, dict]], list[BaseAttribute], None
        ] = None,
        children: Optional[list] = None,
    ) -> None:
        """
        Initialize an HTML element

        Args:
            name (str): The name of the element.
            void_element (bool): Indicates if the element is a void element. Defaults to False.
            attrs: A list of attributes for the element.
                It can also be a dictionary of key,value strings.
                Defaults to None.
            children: A list of child elements. Defaults to None.
        """
        self.tag = tag
        self.attrs = self._resolve_attrs(attrs)

        self._children = children if children else []
        self.is_void_element = void_element

    def __eq__(self, other):
        """Compare rendered HTML instead of class data"""
        if isinstance(other, self.__class__):
            return self.render() == other.render()

        return False

    def _process_attr(self, attr_name, attr_data):
        """
        Add an attribute for the element to the internal _attrs dict
        We technically allow stacking for supported attributes.
        This allows us to support (combine) attributes like "class" and "style".

        Args:
            attr_name (str): The name of the attribute.
            attr_data (Union[str, BaseAttribute]): The data for the attribute.
        """
        if attr_data is None or attr_data is False:
            return  # noop

        if isinstance(attr_data, BaseAttribute):
            attr = attr_data
        else:
            attr_class = SPECIAL_ATTRS.get(attr_name, None)
            if attr_class:
                attr = attr_class(attr_data)
            else:
                attr = BaseAttribute(attr_name, attr_data)

        result = attr.evaluate()
        if result is not None:
            _, resolved_value = result
            if attr_name in self.attrs:
                if attr_name == "class":
                    self.attrs[attr_name] = (
                        f"{self.attrs[attr_name]} {resolved_value}"
                    )
                elif attr_name == "style":
                    self.attrs[attr_name] = (
                        f"{self.attrs[attr_name]}; {resolved_value}"
                    )
                else:
                    raise ValueError(
                        f"Attribute {attr_name} was passed twice. "
                        "We don't know how to merge it."
                    )
            else:
                self.attrs[attr_name] = resolved_value

    def _resolve_attrs(self, attrs) -> dict[str, str]:
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

        else:
            raise ValueError(f"Unknown: {type(attrs)}")

        return attr_dict

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
        else:
            raise ValueError(
                "Lambda received has too many parameters to process"
            )

        return result

    def _resolve_child(
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

        elif isinstance(child, ElementBase):
            # Recursively resolve the element tree
            yield from child.resolve(self)

        elif isinstance(child, _HasHtml):
            # Fetch raw HTML from object
            yield unsafe_text(child.__html__())

        elif isinstance(child, str):
            # Magic: If the string is already escaped, this never has to fire.
            yield escape_text(child)

        elif isinstance(child, int):
            # escape_text will str()
            yield escape_text(child)

        elif isinstance(child, float):
            # Magic: Convert float to string with fixed ndigits
            # This avoids weird output like 6.33333333333...
            precision = self.__class__.FLOAT_PRECISION
            rounded = round(child, precision)
            if precision == 0:
                # Cut off decimal point in this case.
                rounded = int(rounded)
            yield escape_text(rounded)

        elif isinstance(child, bool):
            # Magic: Convert to 'typical' true/false
            # Most people using this would be better using None
            # which specifically means "no render"
            # But some weirdos may be trying to render true/false literally
            yield unsafe_text("true" if child else "false")

        elif util_funcs.is_iterable_but_not_str(child):
            for el in util_funcs.flatten_iterable(child):  # type: ignore[arg-type]
                yield from self._resolve_child(el, call_callables, parent)

        elif callable(child):
            if not call_callables:
                # In deferred resolve state,
                # callables are yielded instead of resolved
                yield child  # type: ignore[misc]
            else:
                result = child
                while callable(result):
                    result = self._call_callable(child, parent)

                yield from self._resolve_child(result, call_callables, parent)
        else:
            raise ValueError(f"Unknown child type: {type(child)}")

    def _resolve_tree(
        self, parent=None
    ) -> Generator[Union[str, Callable], None, None]:
        """
        Walk html element tree and yield all resolved children

        Callables are yielded instead of resolved

        Return:
            escaped (trusted) HTML strings
        """

        for child in self._children:
            yield from self._resolve_child(
                child, call_callables=False, parent=parent
            )

    def append(self, *child_or_childs: Node):
        if self.is_void_element:
            raise ValueError(f"Void element {self.tag} cannot have children")

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
        attrs = self.attrs

        children = None

        if not self.is_void_element:
            children = [child for child in self._resolve_tree(parent)]

        # join_attrs has a configurable lru_cache
        join_attrs = self.get_attr_join()

        # Generate the key="value" pairs for the attributes
        # The value escape step lives here because we trust no
        # previous step in the pipeline.
        # Magic: Security: Escape all attr values
        attr_string = " ".join(
            (join_attrs(k, escape_text(v)) for k, v in attrs.items())
        )

        if self.is_void_element:
            if attr_string:
                yield f"<{self.tag} {attr_string}/>"
            else:
                yield f"<{self.tag}/>"
        else:
            if attr_string:
                yield f"<{self.tag} {attr_string}>"
            else:
                yield f"<{self.tag}>"

            yield from children  # type: ignore[misc]
            yield f"</{self.tag}>"

    def resolve(self, parent=None) -> Generator[str, None, None]:
        """
        Generate the flat HTML [string] iterator for the HTML element
        """
        resolver = self.deferred_resolve(parent)
        for element in resolver:
            if callable(element):
                # Feature: nested calling similar to a functional programming style
                yield from self._resolve_child(
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

    def __repr__(self) -> str:
        children = [
            child for child in util_funcs.flatten_iterable(self._children)
        ]
        children_info = ", ".join(
            repr(child) if not callable(child) else "<callable>"
            for child in children
        )
        astring = ""
        if self.attrs:
            astring = f"{self.attrs}"
        cstring = ""
        if children:
            cstring = f"[{children_info}]"
        return f"{self.__class__.__name__}({astring}){cstring}"

    def __html__(self) -> str:
        """
        Render the HTML element
        """
        return self.render()
