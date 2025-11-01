from . import BaseAttribute
from ..base_types import StrLike


class OptionAttrs:
    """
    This module contains functions for attributes in the 'option' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def disabled(value: bool) -> BaseAttribute:
        """
        "option" attribute: disabled
        Whether the form control is disabled

        Args:
            value:
                Boolean attribute

        Returns:
            An disabled attribute to be added to your element

        """

        return BaseAttribute("disabled", value)

    @staticmethod
    def label(value: StrLike) -> BaseAttribute:
        """
        "option" attribute: label
        User-visible label

        Args:
            value:
                Text

        Returns:
            An label attribute to be added to your element

        """

        return BaseAttribute("label", value)

    @staticmethod
    def selected(value: bool) -> BaseAttribute:
        """
        "option" attribute: selected
        Whether the option is selected by default

        Args:
            value:
                Boolean attribute

        Returns:
            An selected attribute to be added to your element

        """

        return BaseAttribute("selected", value)

    @staticmethod
    def value(value: StrLike) -> BaseAttribute:
        """
        "option" attribute: value
        Value to be used for form submission

        Args:
            value:
                Text

        Returns:
            An value attribute to be added to your element

        """

        return BaseAttribute("value", value)
