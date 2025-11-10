from . import BaseAttribute
from typing import Literal, Iterable, Mapping
from ..base_types import Resolvable, StrLike

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

        Args:
            value:
                ASCII case-insensitive match for "UTF-8"
        
        Returns:
            An accept-charset attribute to be added to your element

        """
        
        return BaseAttribute("accept-charset", value)
            


    @staticmethod
    def action(value) -> BaseAttribute:
        """
        "form" attribute: action  
        URL to use for form submission  

        Args:
            value:
                Valid non-empty URL potentially surrounded by spaces
        
        Returns:
            An action attribute to be added to your element

        """
        
        return BaseAttribute("action", value)
            


    @staticmethod
    def autocomplete(value: Literal['on', 'off']) -> BaseAttribute:
        """
        "form" attribute: autocomplete  
        Default setting for autofill feature for controls in the form  

        Args:
            value:
                ['on', 'off']
        
        Returns:
            An autocomplete attribute to be added to your element

        """
        
        return BaseAttribute("autocomplete", value)
            


    @staticmethod
    def enctype(value: Literal['application/x-www-form-urlencoded', 'multipart/form-data', 'text/plain']) -> BaseAttribute:
        """
        "form" attribute: enctype  
        Entry list encoding type to use for form submission  

        Args:
            value:
                ['application/x-www-form-urlencoded', 'multipart/form-data', 'text/plain']
        
        Returns:
            An enctype attribute to be added to your element

        """
        
        return BaseAttribute("enctype", value)
            


    @staticmethod
    def method(value: Literal['GET', 'POST', 'dialog']) -> BaseAttribute:
        """
        "form" attribute: method  
        Variant to use for form submission  

        Args:
            value:
                ['GET', 'POST', 'dialog']
        
        Returns:
            An method attribute to be added to your element

        """
        
        return BaseAttribute("method", value)
            


    @staticmethod
    def name(value: StrLike) -> BaseAttribute:
        """
        "form" attribute: name  
        Name of form to use in the document.forms API  

        Args:
            value:
                Text*
        
        Returns:
            An name attribute to be added to your element

        """
        
        return BaseAttribute("name", value)
            


    @staticmethod
    def novalidate(value: bool) -> BaseAttribute:
        """
        "form" attribute: novalidate  
        Bypass form control validation for form submission  

        Args:
            value:
                Boolean attribute
        
        Returns:
            An novalidate attribute to be added to your element

        """
        
        return BaseAttribute("novalidate", value)
            


    @staticmethod
    def target(value) -> BaseAttribute:
        """
        "form" attribute: target  
        Navigable for form submission  

        Args:
            value:
                Valid navigable target name or keyword
        
        Returns:
            An target attribute to be added to your element

        """
        
        return BaseAttribute("target", value)
            