from . import BaseAttribute
from ..base_types import StrLike


class FieldsetAttrs:
    """
    This module contains functions for attributes in the 'fieldset' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def disabled(value: bool) -> BaseAttribute:
        """
        "fieldset" attribute: disabled
        Whether the descendant form controls, except any inside legend, are disabled

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
        "fieldset" attribute: form
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
        "fieldset" attribute: name
        Name of the element to use for form submission and in the form.elements API

        Args:
            value:
                Text*

        Returns:
            An name attribute to be added to your element

        """

        return BaseAttribute("name", value)
