from . import BaseAttribute
from typing import Literal
from ..base_types import StrLike


class TextareaAttrs:
    """
    This module contains functions for attributes in the 'textarea' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def autocomplete(value) -> BaseAttribute:
        """
        "textarea" attribute: autocomplete
        Hint for form autofill feature

        Args:
            value:
                Autofill field name and related tokens*

        Returns:
            An autocomplete attribute to be added to your element

        """

        return BaseAttribute("autocomplete", value)

    @staticmethod
    def cols(value) -> BaseAttribute:
        """
        "textarea" attribute: cols
        Maximum number of characters per line

        Args:
            value:
                Valid non-negative integer greater than zero

        Returns:
            An cols attribute to be added to your element

        """

        return BaseAttribute("cols", value)

    @staticmethod
    def dirname(value: StrLike) -> BaseAttribute:
        """
        "textarea" attribute: dirname
        Name of form control to use for sending the element's directionality in form submission

        Args:
            value:
                Text*

        Returns:
            An dirname attribute to be added to your element

        """

        return BaseAttribute("dirname", value)

    @staticmethod
    def disabled(value: bool) -> BaseAttribute:
        """
        "textarea" attribute: disabled
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
        "textarea" attribute: form
        Associates the element with a form element

        Args:
            value:
                ID*

        Returns:
            An form attribute to be added to your element

        """

        return BaseAttribute("form", value)

    @staticmethod
    def maxlength(value: int) -> BaseAttribute:
        """
        "textarea" attribute: maxlength
        Maximum length of value

        Args:
            value:
                Valid non-negative integer

        Returns:
            An maxlength attribute to be added to your element

        """

        return BaseAttribute("maxlength", value)

    @staticmethod
    def minlength(value: int) -> BaseAttribute:
        """
        "textarea" attribute: minlength
        Minimum length of value

        Args:
            value:
                Valid non-negative integer

        Returns:
            An minlength attribute to be added to your element

        """

        return BaseAttribute("minlength", value)

    @staticmethod
    def name(value: StrLike) -> BaseAttribute:
        """
        "textarea" attribute: name
        Name of the element to use for form submission and in the form.elements API

        Args:
            value:
                Text*

        Returns:
            An name attribute to be added to your element

        """

        return BaseAttribute("name", value)

    @staticmethod
    def placeholder(value: StrLike) -> BaseAttribute:
        """
        "textarea" attribute: placeholder
        User-visible label to be placed within the form control

        Args:
            value:
                Text*

        Returns:
            An placeholder attribute to be added to your element

        """

        return BaseAttribute("placeholder", value)

    @staticmethod
    def readonly(value: bool) -> BaseAttribute:
        """
        "textarea" attribute: readonly
        Whether to allow the value to be edited by the user

        Args:
            value:
                Boolean attribute

        Returns:
            An readonly attribute to be added to your element

        """

        return BaseAttribute("readonly", value)

    @staticmethod
    def required(value: bool) -> BaseAttribute:
        """
        "textarea" attribute: required
        Whether the control is required for form submission

        Args:
            value:
                Boolean attribute

        Returns:
            An required attribute to be added to your element

        """

        return BaseAttribute("required", value)

    @staticmethod
    def rows(value) -> BaseAttribute:
        """
        "textarea" attribute: rows
        Number of lines to show

        Args:
            value:
                Valid non-negative integer greater than zero

        Returns:
            An rows attribute to be added to your element

        """

        return BaseAttribute("rows", value)

    @staticmethod
    def wrap(value: Literal["soft", "hard"]) -> BaseAttribute:
        """
        "textarea" attribute: wrap
        How the value of the form control is to be wrapped for form submission

        Args:
            value:
                ['soft', 'hard']

        Returns:
            An wrap attribute to be added to your element

        """

        return BaseAttribute("wrap", value)
