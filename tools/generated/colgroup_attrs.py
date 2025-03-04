from . import BaseAttribute
from typing import Literal, Union

class ColgroupAttrs:
    """ 
    This module contains functions for attributes in the 'colgroup' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def span(value) -> BaseAttribute:
        """
        "colgroup" attribute: span  
        Number of columns spanned by the element  

        :param value: Valid non-negative integer greater than zero  
        :return: An span attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("span", value)
            