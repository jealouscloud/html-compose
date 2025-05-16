from . import BaseAttribute
from typing import Literal


class FormAttrs:
    """
    This module contains functions for attributes in the 'form' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def accept_charset(value) -> BaseAttribute:
        """
        "form" attribute: accept-charset  
        Character encodings to use for form submission  

        :param value: ASCII case-insensitive match for "UTF-8"  
        :return: An accept-charset attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("accept-charset", value)

    @staticmethod
    def action(value) -> BaseAttribute:
        """
        "form" attribute: action  
        URL to use for form submission  

        :param value: Valid non-empty URL potentially surrounded by spaces  
        :return: An action attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("action", value)

    @staticmethod
    def autocomplete(value: Literal["on", "off"]) -> BaseAttribute:
        """
        "form" attribute: autocomplete  
        Default setting for autofill feature for controls in the form  

        :param value: ['on', 'off']  
        :return: An autocomplete attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("autocomplete", value)

    @staticmethod
    def enctype(
        value: Literal[
            "application/x-www-form-urlencoded",
            "multipart/form-data",
            "text/plain",
        ],
    ) -> BaseAttribute:
        """
        "form" attribute: enctype  
        Entry list encoding type to use for form submission  

        :param value: ['application/x-www-form-urlencoded', 'multipart/form-data', 'text/plain']  
        :return: An enctype attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("enctype", value)

    @staticmethod
    def method(value: Literal["GET", "POST", "dialog"]) -> BaseAttribute:
        """
        "form" attribute: method  
        Variant to use for form submission  

        :param value: ['GET', 'POST', 'dialog']  
        :return: An method attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("method", value)

    @staticmethod
    def name(value: str) -> BaseAttribute:
        """
        "form" attribute: name  
        Name of form to use in the document.forms API  

        :param value: Text*  
        :return: An name attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("name", value)

    @staticmethod
    def novalidate(value: bool) -> BaseAttribute:
        """
        "form" attribute: novalidate  
        Bypass form control validation for form submission  

        :param value: Boolean attribute  
        :return: An novalidate attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("novalidate", value)

    @staticmethod
    def target(value) -> BaseAttribute:
        """
        "form" attribute: target  
        Navigable for form submission  

        :param value: Valid navigable target name or keyword  
        :return: An target attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("target", value)
