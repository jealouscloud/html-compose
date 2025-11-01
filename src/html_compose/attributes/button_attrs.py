from . import BaseAttribute
from typing import Literal
from ..base_types import StrLike


class ButtonAttrs:
    """
    This module contains functions for attributes in the 'button' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def disabled(value: bool) -> BaseAttribute:
        """
        "button" attribute: disabled
        Whether the form control is disabled

        Args:
            value:
                Boolean attribute

        Returns:
            An disabled attribute to be added to your element

        """

        return BaseAttribute("disabled", value)

    @staticmethod
    def form(value) -> BaseAttribute:
        """
        "button" attribute: form
        Associates the element with a form element

        Args:
            value:
                ID*

        Returns:
            An form attribute to be added to your element

        """

        return BaseAttribute("form", value)

    @staticmethod
    def formaction(value) -> BaseAttribute:
        """
        "button" attribute: formaction
        URL to use for form submission

        Args:
            value:
                Valid non-empty URL potentially surrounded by spaces

        Returns:
            An formaction attribute to be added to your element

        """

        return BaseAttribute("formaction", value)

    @staticmethod
    def formenctype(
        value: Literal[
            "application/x-www-form-urlencoded",
            "multipart/form-data",
            "text/plain",
        ],
    ) -> BaseAttribute:
        """
        "button" attribute: formenctype
        Entry list encoding type to use for form submission

        Args:
            value:
                ['application/x-www-form-urlencoded', 'multipart/form-data', 'text/plain']

        Returns:
            An formenctype attribute to be added to your element

        """

        return BaseAttribute("formenctype", value)

    @staticmethod
    def formmethod(value: Literal["GET", "POST", "dialog"]) -> BaseAttribute:
        """
        "button" attribute: formmethod
        Variant to use for form submission

        Args:
            value:
                ['GET', 'POST', 'dialog']

        Returns:
            An formmethod attribute to be added to your element

        """

        return BaseAttribute("formmethod", value)

    @staticmethod
    def formnovalidate(value: bool) -> BaseAttribute:
        """
        "button" attribute: formnovalidate
        Bypass form control validation for form submission

        Args:
            value:
                Boolean attribute

        Returns:
            An formnovalidate attribute to be added to your element

        """

        return BaseAttribute("formnovalidate", value)

    @staticmethod
    def formtarget(value) -> BaseAttribute:
        """
        "button" attribute: formtarget
        Navigable for form submission

        Args:
            value:
                Valid navigable target name or keyword

        Returns:
            An formtarget attribute to be added to your element

        """

        return BaseAttribute("formtarget", value)

    @staticmethod
    def name(value: StrLike) -> BaseAttribute:
        """
        "button" attribute: name
        Name of the element to use for form submission and in the form.elements API

        Args:
            value:
                Text*

        Returns:
            An name attribute to be added to your element

        """

        return BaseAttribute("name", value)

    @staticmethod
    def popovertarget(value) -> BaseAttribute:
        """
        "button" attribute: popovertarget
        Targets a popover element to toggle, show, or hide

        Args:
            value:
                ID*

        Returns:
            An popovertarget attribute to be added to your element

        """

        return BaseAttribute("popovertarget", value)

    @staticmethod
    def popovertargetaction(
        value: Literal["toggle", "show", "hide"],
    ) -> BaseAttribute:
        """
        "button" attribute: popovertargetaction
        Indicates whether a targeted popover element is to be toggled, shown, or hidden

        Args:
            value:
                ['toggle', 'show', 'hide']

        Returns:
            An popovertargetaction attribute to be added to your element

        """

        return BaseAttribute("popovertargetaction", value)

    @staticmethod
    def type(value: Literal["submit", "reset", "button"]) -> BaseAttribute:
        """
        "button" attribute: type
        Type of button

        Args:
            value:
                ['submit', 'reset', 'button']

        Returns:
            An type attribute to be added to your element

        """

        return BaseAttribute("type", value)

    @staticmethod
    def value(value: StrLike) -> BaseAttribute:
        """
        "button" attribute: value
        Value to be used for form submission

        Args:
            value:
                Text

        Returns:
            An value attribute to be added to your element

        """

        return BaseAttribute("value", value)
