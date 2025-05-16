from . import BaseAttribute
from typing import Literal, Union

class ButtonAttrs:
    """ 
    This module contains functions for attributes in the 'button' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def disabled(value: bool) -> BaseAttribute:
        """
        "button" attribute: disabled  
        Whether the form control is disabled  

        :param value: Boolean attribute  
        :return: An disabled attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("disabled", value)
            


    @staticmethod
    def form(value) -> BaseAttribute:
        """
        "button" attribute: form  
        Associates the element with a form element  

        :param value: ID*  
        :return: An form attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("form", value)
            


    @staticmethod
    def formaction(value) -> BaseAttribute:
        """
        "button" attribute: formaction  
        URL to use for form submission  

        :param value: Valid non-empty URL potentially surrounded by spaces  
        :return: An formaction attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("formaction", value)
            


    @staticmethod
    def formenctype(value: Literal['application/x-www-form-urlencoded', 'multipart/form-data', 'text/plain']) -> BaseAttribute:
        """
        "button" attribute: formenctype  
        Entry list encoding type to use for form submission  

        :param value: ['application/x-www-form-urlencoded', 'multipart/form-data', 'text/plain']  
        :return: An formenctype attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("formenctype", value)
            


    @staticmethod
    def formmethod(value: Literal['GET', 'POST', 'dialog']) -> BaseAttribute:
        """
        "button" attribute: formmethod  
        Variant to use for form submission  

        :param value: ['GET', 'POST', 'dialog']  
        :return: An formmethod attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("formmethod", value)
            


    @staticmethod
    def formnovalidate(value: bool) -> BaseAttribute:
        """
        "button" attribute: formnovalidate  
        Bypass form control validation for form submission  

        :param value: Boolean attribute  
        :return: An formnovalidate attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("formnovalidate", value)
            


    @staticmethod
    def formtarget(value) -> BaseAttribute:
        """
        "button" attribute: formtarget  
        Navigable for form submission  

        :param value: Valid navigable target name or keyword  
        :return: An formtarget attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("formtarget", value)
            


    @staticmethod
    def name(value: str) -> BaseAttribute:
        """
        "button" attribute: name  
        Name of the element to use for form submission and in the form.elements API  

        :param value: Text*  
        :return: An name attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("name", value)
            


    @staticmethod
    def popovertarget(value) -> BaseAttribute:
        """
        "button" attribute: popovertarget  
        Targets a popover element to toggle, show, or hide  

        :param value: ID*  
        :return: An popovertarget attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("popovertarget", value)
            


    @staticmethod
    def popovertargetaction(value: Literal['toggle', 'show', 'hide']) -> BaseAttribute:
        """
        "button" attribute: popovertargetaction  
        Indicates whether a targeted popover element is to be toggled, shown, or hidden  

        :param value: ['toggle', 'show', 'hide']  
        :return: An popovertargetaction attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("popovertargetaction", value)
            


    @staticmethod
    def type(value: Literal['submit', 'reset', 'button']) -> BaseAttribute:
        """
        "button" attribute: type  
        Type of button  

        :param value: ['submit', 'reset', 'button']  
        :return: An type attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("type", value)
            


    @staticmethod
    def value(value: str) -> BaseAttribute:
        """
        "button" attribute: value  
        Value to be used for form submission  

        :param value: Text  
        :return: An value attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("value", value)
            