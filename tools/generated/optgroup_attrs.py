from . import BaseAttribute
from typing import Literal, Union

class OptgroupAttrs:
    """ 
    This module contains functions for attributes in the 'optgroup' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def disabled(value: bool) -> BaseAttribute:
        """
        "optgroup" attribute: disabled  
        Whether the form control is disabled  

        :param value: Boolean attribute  
        :return: An disabled attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("disabled", value)
            


    @staticmethod
    def label(value: str) -> BaseAttribute:
        """
        "optgroup" attribute: label  
        User-visible label  

        :param value: Text  
        :return: An label attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("label", value)
            