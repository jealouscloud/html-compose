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

        :param value: Valid non-negative integer  
        :return: An height attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("height", value)

    @staticmethod
    def src(value) -> BaseAttribute:
        """
        "embed" attribute: src  
        Address of the resource  

        :param value: Valid non-empty URL potentially surrounded by spaces  
        :return: An src attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("src", value)

    @staticmethod
    def type(value) -> BaseAttribute:
        """
        "embed" attribute: type  
        Type of embedded resource  

        :param value: Valid MIME type string  
        :return: An type attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("type", value)

    @staticmethod
    def width(value: int) -> BaseAttribute:
        """
        "embed" attribute: width  
        Horizontal dimension  

        :param value: Valid non-negative integer  
        :return: An width attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("width", value)
