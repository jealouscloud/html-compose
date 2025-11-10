from . import BaseAttribute
from typing import Literal, Iterable, Mapping
from ..base_types import Resolvable, StrLike

class ColgroupAttrs:
    """ 
    This module contains functions for attributes in the 'colgroup' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def span(value) -> BaseAttribute:
        """
        "colgroup" attribute: span  
        Number of columns spanned by the element  

        Args:
            value:
                Valid non-negative integer greater than zero
        
        Returns:
            An span attribute to be added to your element

        """
        
        return BaseAttribute("span", value)
            