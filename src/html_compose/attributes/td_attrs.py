from . import BaseAttribute
from ..base_types import Resolvable


class TdAttrs:
    """
    This module contains functions for attributes in the 'td' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def colspan(value) -> BaseAttribute:
        """
        "td" attribute: colspan
        Number of columns that the cell is to span

        Args:
            value:
                Valid non-negative integer greater than zero

        Returns:
            An colspan attribute to be added to your element

        """

        return BaseAttribute("colspan", value)

    @staticmethod
    def headers(value: Resolvable) -> BaseAttribute:
        """
        "td" attribute: headers
        The header cells for this cell

        Args:
            value:
                Unordered set of unique space-separated tokens consisting of IDs*

        Returns:
            An headers attribute to be added to your element

        """

        return BaseAttribute("headers", value)

    @staticmethod
    def rowspan(value: int) -> BaseAttribute:
        """
        "td" attribute: rowspan
        Number of rows that the cell is to span

        Args:
            value:
                Valid non-negative integer

        Returns:
            An rowspan attribute to be added to your element

        """

        return BaseAttribute("rowspan", value)
