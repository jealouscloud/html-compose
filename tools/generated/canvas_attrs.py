from . import BaseAttribute
from typing import Literal, Iterable, Mapping
from ..base_types import Resolvable, StrLike

class CanvasAttrs:
    """ 
    This module contains functions for attributes in the 'canvas' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def height(value: int) -> BaseAttribute:
        """
        "canvas" attribute: height  
        Vertical dimension  

        Args:
            value:
                Valid non-negative integer
        
        Returns:
            An height attribute to be added to your element

        """
        
        return BaseAttribute("height", value)
            


    @staticmethod
    def width(value: int) -> BaseAttribute:
        """
        "canvas" attribute: width  
        Horizontal dimension  

        Args:
            value:
                Valid non-negative integer
        
        Returns:
            An width attribute to be added to your element

        """
        
        return BaseAttribute("width", value)
            