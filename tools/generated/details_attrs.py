from . import BaseAttribute
from typing import Literal, Union

class DetailsAttrs:
    """ 
    This module contains functions for attributes in the 'details' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def name(value: str) -> BaseAttribute:
        """
        "details" attribute: name  
        Name of group of mutually-exclusive details elements  

        :param value: Text*  
        :return: An name attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("name", value)
            


    @staticmethod
    def open(value: bool) -> BaseAttribute:
        """
        "details" attribute: open  
        Whether the details are visible  

        :param value: Boolean attribute  
        :return: An open attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("open", value)
            