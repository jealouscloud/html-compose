from . import BaseAttribute
from typing import Literal, Union

class StyleAttrs:
    """ 
    This module contains functions for attributes in the 'style' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def blocking(value: list) -> BaseAttribute:
        """
        "style" attribute: blocking  
        Whether the element is potentially render-blocking  

        :param value: Unordered set of unique space-separated tokens*  
        :return: An blocking attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("blocking", value)
            


    @staticmethod
    def media(value) -> BaseAttribute:
        """
        "style" attribute: media  
        Applicable media  

        :param value: Valid media query list  
        :return: An media attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("media", value)
            


    @staticmethod
    def title(value: str) -> BaseAttribute:
        """
        "style" attribute: title  
        CSS style sheet set name  

        :param value: Text  
        :return: An title attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("title", value)
            