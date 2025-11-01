from . import BaseAttribute


class BlockquoteAttrs:
    """
    This module contains functions for attributes in the 'blockquote' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def cite(value) -> BaseAttribute:
        """
        "blockquote" attribute: cite
        Link to the source of the quotation or more information about the edit

        Args:
            value:
                Valid URL potentially surrounded by spaces

        Returns:
            An cite attribute to be added to your element

        """

        return BaseAttribute("cite", value)
