from . import BaseAttribute
from typing import Literal, Union

class QAttrs:
    """ 
    This module contains functions for attributes in the 'q' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def cite(value) -> BaseAttribute:
        """
        "q" attribute: cite  
        Link to the source of the quotation or more information about the edit  

        :param value: Valid URL potentially surrounded by spaces  
        :return: An cite attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("cite", value)
            