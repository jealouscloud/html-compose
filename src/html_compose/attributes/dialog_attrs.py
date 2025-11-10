from . import BaseAttribute


class DialogAttrs:
    """
    This module contains functions for attributes in the 'dialog' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def open(value: bool) -> BaseAttribute:
        """
        "dialog" attribute: open
        Whether the dialog box is showing

        Args:
            value:
                Boolean attribute

        Returns:
            An open attribute to be added to your element

        """

        return BaseAttribute("open", value)
