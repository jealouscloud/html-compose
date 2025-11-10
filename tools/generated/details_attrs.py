from . import BaseAttribute
from typing import Literal, Iterable, Mapping
from ..base_types import Resolvable, StrLike

class DetailsAttrs:
    """ 
    This module contains functions for attributes in the 'details' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def name(value: StrLike) -> BaseAttribute:
        """
        "details" attribute: name  
        Name of group of mutually-exclusive details elements  

        Args:
            value:
                Text*
        
        Returns:
            An name attribute to be added to your element

        """
        
        return BaseAttribute("name", value)
            


    @staticmethod
    def open(value: bool) -> BaseAttribute:
        """
        "details" attribute: open  
        Whether the details are visible  

        Args:
            value:
                Boolean attribute
        
        Returns:
            An open attribute to be added to your element

        """
        
        return BaseAttribute("open", value)
            