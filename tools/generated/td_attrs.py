from . import BaseAttribute
from typing import Literal, Union

class TdAttrs:
    """ 
    This module contains classes for attributes in the <td> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class colspan(BaseAttribute):
        """
        td attribute: colspan
        Description: Number of columns that the cell is to span
        Value: Valid non-negative integer greater than zero
        """
        
        def __init__(self, value):
            super().__init__("colspan", value)
            


    class headers(BaseAttribute):
        """
        td attribute: headers
        Description: The header cells for this cell
        Value: Unordered set of unique space-separated tokens consisting of IDs*
        """
        
        def __init__(self, value):
            super().__init__("headers", value)
            


    class rowspan(BaseAttribute):
        """
        td attribute: rowspan
        Description: Number of rows that the cell is to span
        Value: Valid non-negative integer
        """
        
        def __init__(self, value: int):
            super().__init__("rowspan", value)
            