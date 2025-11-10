from . import BaseAttribute
from ..base_types import Resolvable, StrLike


class StyleAttrs:
    """
    This module contains functions for attributes in the 'style' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def blocking(value: Resolvable) -> BaseAttribute:
        """
        "style" attribute: blocking
        Whether the element is potentially render-blocking

        Args:
            value:
                Unordered set of unique space-separated tokens*

        Returns:
            An blocking attribute to be added to your element

        """

        return BaseAttribute("blocking", value)

    @staticmethod
    def media(value) -> BaseAttribute:
        """
        "style" attribute: media
        Applicable media

        Args:
            value:
                Valid media query list

        Returns:
            An media attribute to be added to your element

        """

        return BaseAttribute("media", value)

    @staticmethod
    def title(value: StrLike) -> BaseAttribute:
        """
        "style" attribute: title
        CSS style sheet set name

        Args:
            value:
                Text

        Returns:
            An title attribute to be added to your element

        """

        return BaseAttribute("title", value)
