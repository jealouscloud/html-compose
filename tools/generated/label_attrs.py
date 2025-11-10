from . import BaseAttribute
from typing import Literal, Iterable, Mapping
from ..base_types import Resolvable, StrLike

class LabelAttrs:
    """ 
    This module contains functions for attributes in the 'label' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def for_(value) -> BaseAttribute:
        """
        "label" attribute: for  
        Associate the label with form control  

        Args:
            value:
                ID*
        
        Returns:
            An for attribute to be added to your element

        """
        
        return BaseAttribute("for", value)
            