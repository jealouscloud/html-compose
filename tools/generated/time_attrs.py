from . import BaseAttribute
from typing import Literal, Union

class TimeAttrs:
    """ 
    This module contains classes for attributes in the <time> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class datetime(BaseAttribute):
        """
        time attribute: datetime
        Description: Machine-readable value
        Value: Valid month string, valid date string, valid yearless date string, valid time string, valid local date and time string, valid time-zone offset string, valid global date and time string, valid week string, valid non-negative integer, or valid duration string
        """
        
        def __init__(self, value):
            super().__init__("datetime", value)
            