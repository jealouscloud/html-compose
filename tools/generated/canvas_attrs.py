from . import BaseAttribute
from typing import Literal, Union, Callable

class CanvasAttrs:
    """ 
    This module contains classes for attributes in the <canvas> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class height(BaseAttribute):
        """
        canvas attribute: height
        Description: Vertical dimension
        Value: Valid non-negative integer
        """
        
        def __init__(self, value):
            super().__init__("height", value)
            


    class width(BaseAttribute):
        """
        canvas attribute: width
        Description: Horizontal dimension
        Value: Valid non-negative integer
        """
        
        def __init__(self, value):
            super().__init__("width", value)
            