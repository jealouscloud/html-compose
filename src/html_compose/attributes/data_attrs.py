from . import BaseAttribute


class DataAttrs:
    """
    This module contains functions for attributes in the 'data' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def value(value: str) -> BaseAttribute:
        """
        "data" attribute: value  
        Machine-readable value  

        :param value: Text*  
        :return: An value attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("value", value)
