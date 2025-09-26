from typing import Iterable, Mapping

from .attributes import BaseAttribute, GlobalAttrs
from .base_element import BaseElement
from .base_types import Resolvable
from .util_funcs import safe_name


class CustomElement(BaseElement):
    """
    Custom HTML element
    """

    tag = "UNSET"
    is_void = False

    def __init__(
        self,
        attrs: Iterable[BaseAttribute]
        | Mapping[str, Resolvable]
        | Iterable[
            BaseAttribute | Iterable[BaseAttribute] | Mapping[str, Resolvable]
        ]
        | None = None,
        id: str | None = None,
        class_: str | list | None = None,
        children: list | None = None,
    ):
        """
        Initialize a custom HTML element


        Parameters
        ----------
        `attrs`:
            A list or dictionary of attributes for the element

        `id` :
            The element's ID

        `class_` :
            Classes to which the element belongs

        `children` :
            A list of child elements. Defaults to None.

        """
        tag = self.__class__.tag
        if tag == "UNSET":
            raise ValueError(
                "CustomElement must be created with a tag name using the create() method."
            )
        super().__init__(
            self.__class__.tag,
            void_element=self.__class__.is_void,
            attrs=attrs,
            children=children,
        )
        if not (id is None or id is False):
            self._process_attr("id", id)
        if not (class_ is None or class_ is False):
            self._process_attr("class", class_)

    class hint(GlobalAttrs):
        pass

    _ = hint

    @staticmethod
    def create(tag: str, void_element: bool = False) -> type["CustomElement"]:
        """
        Create a new element class with the given tag and void_element flag.
        This method is a factory for creating new element classes.
        """
        return type(
            safe_name(tag),
            (CustomElement,),
            {"tag": tag, "is_void": void_element},
        )
