from . import BaseAttribute
from typing import Literal, Union

class BaseAttrs:
    """ 
    This module contains functions for attributes in the 'base' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def href(value) -> BaseAttribute:
        """
        "base" attribute: href  
        Document base URL  

        :param value: Valid URL potentially surrounded by spaces  
        :return: An href attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("href", value)
            


    @staticmethod
    def target(value) -> BaseAttribute:
        """
        "base" attribute: target  
        Default navigable for hyperlink navigation and form submission  

        :param value: Valid navigable target name or keyword  
        :return: An target attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("target", value)
            