from . import BaseAttribute
from typing import Literal, Union

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

        :param value: ['ltr', 'rtl']  
        :return: An dir attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("dir", value)
            