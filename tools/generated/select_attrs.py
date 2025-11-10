from . import BaseAttribute
from typing import Literal, Iterable, Mapping
from ..base_types import Resolvable, StrLike

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

        Args:
            value:
                Autofill field name and related tokens*
        
        Returns:
            An autocomplete attribute to be added to your element

        """
        
        return BaseAttribute("autocomplete", value)
            


    @staticmethod
    def disabled(value: bool) -> BaseAttribute:
        """
        "select" attribute: disabled  
        Whether the form control is disabled  

        Args:
            value:
                Boolean attribute
        
        Returns:
            An disabled attribute to be added to your element

        """
        
        return BaseAttribute("disabled", value)
            


    @staticmethod
    def form(value) -> BaseAttribute:
        """
        "select" attribute: form  
        Associates the element with a form element  

        Args:
            value:
                ID*
        
        Returns:
            An form attribute to be added to your element

        """
        
        return BaseAttribute("form", value)
            


    @staticmethod
    def multiple(value: bool) -> BaseAttribute:
        """
        "select" attribute: multiple  
        Whether to allow multiple values  

        Args:
            value:
                Boolean attribute
        
        Returns:
            An multiple attribute to be added to your element

        """
        
        return BaseAttribute("multiple", value)
            


    @staticmethod
    def name(value: StrLike) -> BaseAttribute:
        """
        "select" attribute: name  
        Name of the element to use for form submission and in the form.elements API  

        Args:
            value:
                Text*
        
        Returns:
            An name attribute to be added to your element

        """
        
        return BaseAttribute("name", value)
            


    @staticmethod
    def required(value: bool) -> BaseAttribute:
        """
        "select" attribute: required  
        Whether the control is required for form submission  

        Args:
            value:
                Boolean attribute
        
        Returns:
            An required attribute to be added to your element

        """
        
        return BaseAttribute("required", value)
            


    @staticmethod
    def size(value) -> BaseAttribute:
        """
        "select" attribute: size  
        Size of the control  

        Args:
            value:
                Valid non-negative integer greater than zero
        
        Returns:
            An size attribute to be added to your element

        """
        
        return BaseAttribute("size", value)
            