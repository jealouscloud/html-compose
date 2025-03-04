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

        :param value: Valid non-negative integer  
        :return: An height attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("height", value)

    @staticmethod
    def media(value) -> BaseAttribute:
        """
        "source" attribute: media  
        Applicable media  

        :param value: Valid media query list  
        :return: An media attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("media", value)

    @staticmethod
    def sizes(value) -> BaseAttribute:
        """
        "source" attribute: sizes  
        Image sizes for different page layouts  

        :param value: Valid source size list  
        :return: An sizes attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("sizes", value)

    @staticmethod
    def src(value) -> BaseAttribute:
        """
        "source" attribute: src  
        Address of the resource  

        :param value: Valid non-empty URL potentially surrounded by spaces  
        :return: An src attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("src", value)

    @staticmethod
    def srcset(value) -> BaseAttribute:
        """
        "source" attribute: srcset  
        Images to use in different situations, e.g., high-resolution displays, small monitors, etc.  

        :param value: Comma-separated list of image candidate strings  
        :return: An srcset attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("srcset", value)

    @staticmethod
    def type(value) -> BaseAttribute:
        """
        "source" attribute: type  
        Type of embedded resource  

        :param value: Valid MIME type string  
        :return: An type attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("type", value)

    @staticmethod
    def width(value: int) -> BaseAttribute:
        """
        "source" attribute: width  
        Horizontal dimension  

        :param value: Valid non-negative integer  
        :return: An width attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("width", value)
