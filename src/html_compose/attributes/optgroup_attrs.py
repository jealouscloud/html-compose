from . import BaseAttribute
from ..base_types import StrLike


class OptgroupAttrs:
    """
    This module contains functions for attributes in the 'optgroup' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def disabled(value: bool) -> BaseAttribute:
        """
        "optgroup" attribute: disabled
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
        "optgroup" attribute: label
        User-visible label

        Args:
            value:
                Text

        Returns:
            An label attribute to be added to your element

        """

        return BaseAttribute("label", value)
