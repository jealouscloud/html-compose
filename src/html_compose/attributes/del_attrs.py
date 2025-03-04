from . import BaseAttribute


class DelAttrs:
    """
    This module contains functions for attributes in the 'del' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def cite(value) -> BaseAttribute:
        """
        "del" attribute: cite  
        Link to the source of the quotation or more information about the edit  

        :param value: Valid URL potentially surrounded by spaces  
        :return: An cite attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("cite", value)

    @staticmethod
    def datetime(value) -> BaseAttribute:
        """
        "del" attribute: datetime  
        Date and (optionally) time of the change  

        :param value: Valid date string with optional time  
        :return: An datetime attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("datetime", value)
