from . import BaseAttribute
from typing import Literal, Iterable, Mapping
from ..base_types import Resolvable, StrLike

class LiAttrs:
    """ 
    This module contains functions for attributes in the 'li' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def value(value: int) -> BaseAttribute:
        """
        "li" attribute: value  
        Ordinal value of the list item  

        Args:
            value:
                Valid integer
        
        Returns:
            An value attribute to be added to your element

        """
        
        return BaseAttribute("value", value)
            