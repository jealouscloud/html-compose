from . import BaseAttribute


class CanvasAttrs:
    """
    This module contains functions for attributes in the 'canvas' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def height(value: int) -> BaseAttribute:
        """
        "canvas" attribute: height  
        Vertical dimension  

        :param value: Valid non-negative integer  
        :return: An height attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("height", value)

    @staticmethod
    def width(value: int) -> BaseAttribute:
        """
        "canvas" attribute: width  
        Horizontal dimension  

        :param value: Valid non-negative integer  
        :return: An width attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("width", value)
