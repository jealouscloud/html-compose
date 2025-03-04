from . import BaseAttribute
from typing import Literal, Union

class TimeAttrs:
    """ 
    This module contains functions for attributes in the 'time' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def datetime(value) -> BaseAttribute:
        """
        "time" attribute: datetime  
        Machine-readable value  

        :param value: Valid month string, valid date string, valid yearless date string, valid time string, valid local date and time string, valid time-zone offset string, valid global date and time string, valid week string, valid non-negative integer, or valid duration string  
        :return: An datetime attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("datetime", value)
            