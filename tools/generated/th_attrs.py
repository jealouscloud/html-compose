from . import BaseAttribute
from typing import Literal, Union

class ThAttrs:
    """ 
    This module contains functions for attributes in the 'th' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def abbr(value: str) -> BaseAttribute:
        """
        "th" attribute: abbr  
        Alternative label to use for the header cell when referencing the cell in other contexts  

        :param value: Text*  
        :return: An abbr attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("abbr", value)
            


    @staticmethod
    def colspan(value) -> BaseAttribute:
        """
        "th" attribute: colspan  
        Number of columns that the cell is to span  

        :param value: Valid non-negative integer greater than zero  
        :return: An colspan attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("colspan", value)
            


    @staticmethod
    def headers(value: list) -> BaseAttribute:
        """
        "th" attribute: headers  
        The header cells for this cell  

        :param value: Unordered set of unique space-separated tokens consisting of IDs*  
        :return: An headers attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("headers", value)
            


    @staticmethod
    def rowspan(value: int) -> BaseAttribute:
        """
        "th" attribute: rowspan  
        Number of rows that the cell is to span  

        :param value: Valid non-negative integer  
        :return: An rowspan attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("rowspan", value)
            


    @staticmethod
    def scope(value: Literal['row', 'col', 'rowgroup', 'colgroup']) -> BaseAttribute:
        """
        "th" attribute: scope  
        Specifies which cells the header cell applies to  

        :param value: ['row', 'col', 'rowgroup', 'colgroup']  
        :return: An scope attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("scope", value)
            