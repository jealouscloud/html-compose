from . import BaseAttribute
from typing import Literal, Union

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

        :param value: ID*  
        :return: An for attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("for", value)
            