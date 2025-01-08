from . import BaseAttribute
from typing import Literal, Union

class MapAttrs:
    """ 
    This module contains classes for attributes in the <map> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class name(BaseAttribute):
        """
        map attribute: name
        Description: Name of image map to reference from the usemap attribute
        Value: Text*
        """
        
        def __init__(self, value: str):
            super().__init__("name", value)
            