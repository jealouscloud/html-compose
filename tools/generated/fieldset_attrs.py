from . import BaseAttribute
from typing import Literal, Union

class FieldsetAttrs:
    """ 
    This module contains functions for attributes in the 'fieldset' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def disabled(value: bool) -> BaseAttribute:
        """
        "fieldset" attribute: disabled  
        Whether the descendant form controls, except any inside legend, are disabled  

        :param value: Boolean attribute  
        :return: An disabled attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("disabled", value)
            


    @staticmethod
    def form(value) -> BaseAttribute:
        """
        "fieldset" attribute: form  
        Associates the element with a form element  

        :param value: ID*  
        :return: An form attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("form", value)
            


    @staticmethod
    def name(value: str) -> BaseAttribute:
        """
        "fieldset" attribute: name  
        Name of the element to use for form submission and in the form.elements API  

        :param value: Text*  
        :return: An name attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("name", value)
            