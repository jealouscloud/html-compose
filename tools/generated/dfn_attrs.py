from . import BaseAttribute
from typing import Literal, Iterable, Mapping
from ..base_types import Resolvable, StrLike

class DfnAttrs:
    """ 
    This module contains functions for attributes in the 'dfn' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def title(value: StrLike) -> BaseAttribute:
        """
        "dfn" attribute: title  
        Full term or expansion of abbreviation  

        Args:
            value:
                Text
        
        Returns:
            An title attribute to be added to your element

        """
        
        return BaseAttribute("title", value)
            