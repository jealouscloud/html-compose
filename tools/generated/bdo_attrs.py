from . import BaseAttribute
from typing import Literal, Iterable, Mapping
from ..base_types import Resolvable, StrLike

class BdoAttrs:
    """ 
    This module contains functions for attributes in the 'bdo' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def dir(value: Literal['ltr', 'rtl']) -> BaseAttribute:
        """
        "bdo" attribute: dir  
        The text directionality of the element  

        Args:
            value:
                ['ltr', 'rtl']
        
        Returns:
            An dir attribute to be added to your element

        """
        
        return BaseAttribute("dir", value)
            