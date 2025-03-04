from . import BaseAttribute


class OptionAttrs:
    """
    This module contains functions for attributes in the 'option' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def disabled(value: bool) -> BaseAttribute:
        """
        "option" attribute: disabled  
        Whether the form control is disabled  

        :param value: Boolean attribute  
        :return: An disabled attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("disabled", value)

    @staticmethod
    def label(value: str) -> BaseAttribute:
        """
        "option" attribute: label  
        User-visible label  

        :param value: Text  
        :return: An label attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("label", value)

    @staticmethod
    def selected(value: bool) -> BaseAttribute:
        """
        "option" attribute: selected  
        Whether the option is selected by default  

        :param value: Boolean attribute  
        :return: An selected attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("selected", value)

    @staticmethod
    def value(value: str) -> BaseAttribute:
        """
        "option" attribute: value  
        Value to be used for form submission  

        :param value: Text  
        :return: An value attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("value", value)
