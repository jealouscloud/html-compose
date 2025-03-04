from . import BaseAttribute


class ProgressAttrs:
    """
    This module contains functions for attributes in the 'progress' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def max(value: float) -> BaseAttribute:
        """
        "progress" attribute: max  
        Upper bound of range  

        :param value: Valid floating-point number*  
        :return: An max attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("max", value)

    @staticmethod
    def value(value: float) -> BaseAttribute:
        """
        "progress" attribute: value  
        Current value of the element  

        :param value: Valid floating-point number  
        :return: An value attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("value", value)
