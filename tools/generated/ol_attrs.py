from . import BaseAttribute
from typing import Literal, Iterable, Mapping
from ..base_types import Resolvable, StrLike

class OlAttrs:
    """ 
    This module contains functions for attributes in the 'ol' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def reversed(value: bool) -> BaseAttribute:
        """
        "ol" attribute: reversed  
        Number the list backwards  

        Args:
            value:
                Boolean attribute
        
        Returns:
            An reversed attribute to be added to your element

        """
        
        return BaseAttribute("reversed", value)
            


    @staticmethod
    def start(value: int) -> BaseAttribute:
        """
        "ol" attribute: start  
        Starting value of the list  

        Args:
            value:
                Valid integer
        
        Returns:
            An start attribute to be added to your element

        """
        
        return BaseAttribute("start", value)
            


    @staticmethod
    def type(value: Literal['1', 'a', 'A', 'i', 'I']) -> BaseAttribute:
        """
        "ol" attribute: type  
        Kind of list marker  

        Args:
            value:
                ['1', 'a', 'A', 'i', 'I']
        
        Returns:
            An type attribute to be added to your element

        """
        
        return BaseAttribute("type", value)
            