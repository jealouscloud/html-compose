from . import BaseAttribute


class EmbedAttrs:
    """
    This module contains functions for attributes in the 'embed' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def height(value: int) -> BaseAttribute:
        """
        "embed" attribute: height
        Vertical dimension

        Args:
            value:
                Valid non-negative integer

        Returns:
            An height attribute to be added to your element

        """

        return BaseAttribute("height", value)

    @staticmethod
    def src(value) -> BaseAttribute:
        """
        "embed" attribute: src
        Address of the resource

        Args:
            value:
                Valid non-empty URL potentially surrounded by spaces

        Returns:
            An src attribute to be added to your element

        """

        return BaseAttribute("src", value)

    @staticmethod
    def type(value) -> BaseAttribute:
        """
        "embed" attribute: type
        Type of embedded resource

        Args:
            value:
                Valid MIME type string

        Returns:
            An type attribute to be added to your element

        """

        return BaseAttribute("type", value)

    @staticmethod
    def width(value: int) -> BaseAttribute:
        """
        "embed" attribute: width
        Horizontal dimension

        Args:
            value:
                Valid non-negative integer

        Returns:
            An width attribute to be added to your element

        """

        return BaseAttribute("width", value)
