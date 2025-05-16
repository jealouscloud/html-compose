from . import BaseAttribute
from typing import Literal, Union

class TdAttrs:
    """ 
    This module contains functions for attributes in the 'td' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def colspan(value) -> BaseAttribute:
        """
        "td" attribute: colspan  
        Number of columns that the cell is to span  

        :param value: Valid non-negative integer greater than zero  
        :return: An colspan attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("colspan", value)
            


    @staticmethod
    def headers(value: list) -> BaseAttribute:
        """
        "td" attribute: headers  
        The header cells for this cell  

        :param value: Unordered set of unique space-separated tokens consisting of IDs*  
        :return: An headers attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("headers", value)
            


    @staticmethod
    def rowspan(value: int) -> BaseAttribute:
        """
        "td" attribute: rowspan  
        Number of rows that the cell is to span  

        :param value: Valid non-negative integer  
        :return: An rowspan attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("rowspan", value)
            