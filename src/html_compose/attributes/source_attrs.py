from . import BaseAttribute


class SourceAttrs:
    """
    This module contains functions for attributes in the 'source' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def height(value: int) -> BaseAttribute:
        """
        "source" attribute: height
        Vertical dimension

        Args:
            value:
                Valid non-negative integer

        Returns:
            An height attribute to be added to your element

        """

        return BaseAttribute("height", value)

    @staticmethod
    def media(value) -> BaseAttribute:
        """
        "source" attribute: media
        Applicable media

        Args:
            value:
                Valid media query list

        Returns:
            An media attribute to be added to your element

        """

        return BaseAttribute("media", value)

    @staticmethod
    def sizes(value) -> BaseAttribute:
        """
        "source" attribute: sizes
        Image sizes for different page layouts

        Args:
            value:
                Valid source size list

        Returns:
            An sizes attribute to be added to your element

        """

        return BaseAttribute("sizes", value)

    @staticmethod
    def src(value) -> BaseAttribute:
        """
        "source" attribute: src
        Address of the resource

        Args:
            value:
                Valid non-empty URL potentially surrounded by spaces

        Returns:
            An src attribute to be added to your element

        """

        return BaseAttribute("src", value)

    @staticmethod
    def srcset(value) -> BaseAttribute:
        """
        "source" attribute: srcset
        Images to use in different situations, e.g., high-resolution displays, small monitors, etc.

        Args:
            value:
                Comma-separated list of image candidate strings

        Returns:
            An srcset attribute to be added to your element

        """

        return BaseAttribute("srcset", value)

    @staticmethod
    def type(value) -> BaseAttribute:
        """
        "source" attribute: type
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
        "source" attribute: width
        Horizontal dimension

        Args:
            value:
                Valid non-negative integer

        Returns:
            An width attribute to be added to your element

        """

        return BaseAttribute("width", value)
