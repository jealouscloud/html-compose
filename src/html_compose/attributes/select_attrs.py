from . import BaseAttribute


class SelectAttrs:
    """
    This module contains functions for attributes in the 'select' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def autocomplete(value) -> BaseAttribute:
        """
        "select" attribute: autocomplete  
        Hint for form autofill feature  

        :param value: Autofill field name and related tokens*  
        :return: An autocomplete attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("autocomplete", value)

    @staticmethod
    def disabled(value: bool) -> BaseAttribute:
        """
        "select" attribute: disabled  
        Whether the form control is disabled  

        :param value: Boolean attribute  
        :return: An disabled attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("disabled", value)

    @staticmethod
    def form(value) -> BaseAttribute:
        """
        "select" attribute: form  
        Associates the element with a form element  

        :param value: ID*  
        :return: An form attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("form", value)

    @staticmethod
    def multiple(value: bool) -> BaseAttribute:
        """
        "select" attribute: multiple  
        Whether to allow multiple values  

        :param value: Boolean attribute  
        :return: An multiple attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("multiple", value)

    @staticmethod
    def name(value: str) -> BaseAttribute:
        """
        "select" attribute: name  
        Name of the element to use for form submission and in the form.elements API  

        :param value: Text*  
        :return: An name attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("name", value)

    @staticmethod
    def required(value: bool) -> BaseAttribute:
        """
        "select" attribute: required  
        Whether the control is required for form submission  

        :param value: Boolean attribute  
        :return: An required attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("required", value)

    @staticmethod
    def size(value) -> BaseAttribute:
        """
        "select" attribute: size  
        Size of the control  

        :param value: Valid non-negative integer greater than zero  
        :return: An size attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("size", value)
