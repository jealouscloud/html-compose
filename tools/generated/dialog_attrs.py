from . import BaseAttribute
from typing import Literal, Union

class DialogAttrs:
    """ 
    This module contains functions for attributes in the 'dialog' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def open(value: bool) -> BaseAttribute:
        """
        "dialog" attribute: open  
        Whether the dialog box is showing  

        :param value: Boolean attribute  
        :return: An open attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("open", value)
            