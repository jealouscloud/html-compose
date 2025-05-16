from . import BaseAttribute


class OutputAttrs:
    """
    This module contains functions for attributes in the 'output' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def for_(value: list) -> BaseAttribute:
        """
        "output" attribute: for  
        Specifies controls from which the output was calculated  

        :param value: Unordered set of unique space-separated tokens consisting of IDs*  
        :return: An for attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("for", value)

    @staticmethod
    def form(value) -> BaseAttribute:
        """
        "output" attribute: form  
        Associates the element with a form element  

        :param value: ID*  
        :return: An form attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("form", value)

    @staticmethod
    def name(value: str) -> BaseAttribute:
        """
        "output" attribute: name  
        Name of the element to use for form submission and in the form.elements API  

        :param value: Text*  
        :return: An name attribute to be added to your element
        """  # fmt: skip

        return BaseAttribute("name", value)
