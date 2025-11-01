from . import BaseAttribute
from typing import Literal, Iterable, Mapping
from ..base_types import Resolvable, StrLike

class MapAttrs:
    """ 
    This module contains functions for attributes in the 'map' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def name(value: StrLike) -> BaseAttribute:
        """
        "map" attribute: name  
        Name of image map to reference from the usemap attribute  

        Args:
            value:
                Text*
        
        Returns:
            An name attribute to be added to your element

        """
        
        return BaseAttribute("name", value)
            