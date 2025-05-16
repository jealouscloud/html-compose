from . import BaseAttribute
from typing import Literal


class TextareaAttrs:
    """
    This module contains functions for attributes in the 'textarea' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def autocomplete(value) -> BaseAttribute:
        """
        "textarea" attribute: autocomplete  
        Hint for form autofill feature  

        :param value: Autofill field name and related tokens*  
        :return: An autocomplete attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("autocomplete", value)

    @staticmethod
    def cols(value) -> BaseAttribute:
        """
        "textarea" attribute: cols  
        Maximum number of characters per line  

        :param value: Valid non-negative integer greater than zero  
        :return: An cols attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("cols", value)

    @staticmethod
    def dirname(value: str) -> BaseAttribute:
        """
        "textarea" attribute: dirname  
        Name of form control to use for sending the element's directionality in form submission  

        :param value: Text*  
        :return: An dirname attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("dirname", value)

    @staticmethod
    def disabled(value: bool) -> BaseAttribute:
        """
        "textarea" attribute: disabled  
        Whether the form control is disabled  

        :param value: Boolean attribute  
        :return: An disabled attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("disabled", value)

    @staticmethod
    def form(value) -> BaseAttribute:
        """
        "textarea" attribute: form  
        Associates the element with a form element  

        :param value: ID*  
        :return: An form attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("form", value)

    @staticmethod
    def maxlength(value: int) -> BaseAttribute:
        """
        "textarea" attribute: maxlength  
        Maximum length of value  

        :param value: Valid non-negative integer  
        :return: An maxlength attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("maxlength", value)

    @staticmethod
    def minlength(value: int) -> BaseAttribute:
        """
        "textarea" attribute: minlength  
        Minimum length of value  

        :param value: Valid non-negative integer  
        :return: An minlength attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("minlength", value)

    @staticmethod
    def name(value: str) -> BaseAttribute:
        """
        "textarea" attribute: name  
        Name of the element to use for form submission and in the form.elements API  

        :param value: Text*  
        :return: An name attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("name", value)

    @staticmethod
    def placeholder(value: str) -> BaseAttribute:
        """
        "textarea" attribute: placeholder  
        User-visible label to be placed within the form control  

        :param value: Text*  
        :return: An placeholder attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("placeholder", value)

    @staticmethod
    def readonly(value: bool) -> BaseAttribute:
        """
        "textarea" attribute: readonly  
        Whether to allow the value to be edited by the user  

        :param value: Boolean attribute  
        :return: An readonly attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("readonly", value)

    @staticmethod
    def required(value: bool) -> BaseAttribute:
        """
        "textarea" attribute: required  
        Whether the control is required for form submission  

        :param value: Boolean attribute  
        :return: An required attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("required", value)

    @staticmethod
    def rows(value) -> BaseAttribute:
        """
        "textarea" attribute: rows  
        Number of lines to show  

        :param value: Valid non-negative integer greater than zero  
        :return: An rows attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("rows", value)

    @staticmethod
    def wrap(value: Literal["soft", "hard"]) -> BaseAttribute:
        """
        "textarea" attribute: wrap  
        How the value of the form control is to be wrapped for form submission  

        :param value: ['soft', 'hard']  
        :return: An wrap attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("wrap", value)
