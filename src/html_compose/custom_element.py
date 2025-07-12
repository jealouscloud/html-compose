from typing import Optional, Union

from .attributes import BaseAttribute, GlobalAttrs
from .base_element import BaseElement
from .util_funcs import safe_name


class CustomElement(BaseElement):
    tag = "UNSET"
    is_void = False

    def __init__(
        self,
        attrs: Optional[
            Union[dict[str, Union[str, dict, list]], list[BaseAttribute]]
        ] = None,
        id: Optional[str] = None,
        class_: Optional[Union[str, list]] = None,
        children: Optional[list] = None,
    ):
        """
        Initialize a custom HTML element

        Args:
            attrs: A list of attributes for the element.
                It can also be a dictionary of key,value strings.
                Defaults to None.
            id (str): The ID of the element. Defaults to None.
            class_: The class of the element. Defaults to None.
            children: A list of child elements. Defaults to None.
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
