from . import BaseAttribute


class ObjectAttrs:
    """
    This module contains functions for attributes in the 'object' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def data(value) -> BaseAttribute:
        """
        "object" attribute: data
        Address of the resource

        Args:
            value:
                Valid non-empty URL potentially surrounded by spaces

        Returns:
            An data attribute to be added to your element

        """

        return BaseAttribute("data", value)

    @staticmethod
    def form(value) -> BaseAttribute:
        """
        "object" attribute: form
        Associates the element with a form element

        Args:
            value:
                ID*

        Returns:
            An form attribute to be added to your element

        """

        return BaseAttribute("form", value)

    @staticmethod
    def height(value: int) -> BaseAttribute:
        """
        "object" attribute: height
        Vertical dimension

        Args:
            value:
                Valid non-negative integer

        Returns:
            An height attribute to be added to your element

        """

        return BaseAttribute("height", value)

    @staticmethod
    def name(value) -> BaseAttribute:
        """
        "object" attribute: name
        Name of content navigable

        Args:
            value:
                Valid navigable target name or keyword

        Returns:
            An name attribute to be added to your element

        """

        return BaseAttribute("name", value)

    @staticmethod
    def type(value) -> BaseAttribute:
        """
        "object" attribute: type
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
        "object" attribute: width
        Horizontal dimension

        Args:
            value:
                Valid non-negative integer

        Returns:
            An width attribute to be added to your element

        """

        return BaseAttribute("width", value)
