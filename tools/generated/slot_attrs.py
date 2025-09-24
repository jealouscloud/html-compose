from . import BaseAttribute
from typing import Literal, Union
from ..base_types import Resolvable, StrLike

class SlotAttrs:
    """ 
    This module contains functions for attributes in the 'slot' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def name(value: StrLike) -> BaseAttribute:
        """
        "slot" attribute: name  
        Name of shadow tree slot  

        :param value: Text  
        :return: An name attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("name", value)
            