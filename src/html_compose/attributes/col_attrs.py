from . import BaseAttribute


class ColAttrs:
    """
    This module contains functions for attributes in the 'col' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def span(value) -> BaseAttribute:
        """
        "col" attribute: span
        Number of columns spanned by the element

        Args:
            value:
                Valid non-negative integer greater than zero

        Returns:
            An span attribute to be added to your element

        """

        return BaseAttribute("span", value)
