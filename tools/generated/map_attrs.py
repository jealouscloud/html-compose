from . import BaseAttribute
from typing import Literal, Union
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

        :param value: Text*  
        :return: An name attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("name", value)
            