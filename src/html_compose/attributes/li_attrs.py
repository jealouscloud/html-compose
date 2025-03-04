from . import BaseAttribute


class LiAttrs:
    """
    This module contains functions for attributes in the 'li' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def value(value: int) -> BaseAttribute:
        """
        "li" attribute: value  
        Ordinal value of the list item  

        :param value: Valid integer  
        :return: An value attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("value", value)
