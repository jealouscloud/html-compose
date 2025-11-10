from . import BaseAttribute
from ..base_types import Resolvable, StrLike


class OutputAttrs:
    """
    This module contains functions for attributes in the 'output' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def for_(value: Resolvable) -> BaseAttribute:
        """
        "output" attribute: for
        Specifies controls from which the output was calculated

        Args:
            value:
                Unordered set of unique space-separated tokens consisting of IDs*

        Returns:
            An for attribute to be added to your element

        """

        return BaseAttribute("for", value)

    @staticmethod
    def form(value) -> BaseAttribute:
        """
        "output" attribute: form
        Associates the element with a form element

        Args:
            value:
                ID*

        Returns:
            An form attribute to be added to your element

        """

        return BaseAttribute("form", value)

    @staticmethod
    def name(value: StrLike) -> BaseAttribute:
        """
        "output" attribute: name
        Name of the element to use for form submission and in the form.elements API

        Args:
            value:
                Text*

        Returns:
            An name attribute to be added to your element

        """

        return BaseAttribute("name", value)
