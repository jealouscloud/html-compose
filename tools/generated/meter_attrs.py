from . import BaseAttribute
from typing import Literal, Union

class MeterAttrs:
    """ 
    This module contains classes for attributes in the <meter> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class high(BaseAttribute):
        """
        meter attribute: high
        Description: Low limit of high range
        Value: Valid floating-point number*
        """
        
        def __init__(self, value: float):
            super().__init__("high", value)
            


    class low(BaseAttribute):
        """
        meter attribute: low
        Description: High limit of low range
        Value: Valid floating-point number*
        """
        
        def __init__(self, value: float):
            super().__init__("low", value)
            


    class max(BaseAttribute):
        """
        meter attribute: max
        Description: Upper bound of range
        Value: Valid floating-point number*
        """
        
        def __init__(self, value: float):
            super().__init__("max", value)
            


    class min(BaseAttribute):
        """
        meter attribute: min
        Description: Lower bound of range
        Value: Valid floating-point number*
        """
        
        def __init__(self, value: float):
            super().__init__("min", value)
            


    class optimum(BaseAttribute):
        """
        meter attribute: optimum
        Description: Optimum value in gauge
        Value: Valid floating-point number*
        """
        
        def __init__(self, value: float):
            super().__init__("optimum", value)
            


    class value(BaseAttribute):
        """
        meter attribute: value
        Description: Current value of the element
        Value: Valid floating-point number
        """
        
        def __init__(self, value: float):
            super().__init__("value", value)
            