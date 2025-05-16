from . import BaseAttribute
from typing import Literal


class OlAttrs:
    """
    This module contains functions for attributes in the 'ol' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def reversed(value: bool) -> BaseAttribute:
        """
        "ol" attribute: reversed  
        Number the list backwards  

        :param value: Boolean attribute  
        :return: An reversed attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("reversed", value)

    @staticmethod
    def start(value: int) -> BaseAttribute:
        """
        "ol" attribute: start  
        Starting value of the list  

        :param value: Valid integer  
        :return: An start attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("start", value)

    @staticmethod
    def type(value: Literal["1", "a", "A", "i", "I"]) -> BaseAttribute:
        """
        "ol" attribute: type  
        Kind of list marker  

        :param value: ['1', 'a', 'A', 'i', 'I']  
        :return: An type attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("type", value)
