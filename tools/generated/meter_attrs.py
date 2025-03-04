from . import BaseAttribute
from typing import Literal, Union

class MeterAttrs:
    """ 
    This module contains functions for attributes in the 'meter' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def high(value: float) -> BaseAttribute:
        """
        "meter" attribute: high  
        Low limit of high range  

        :param value: Valid floating-point number*  
        :return: An high attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("high", value)
            


    @staticmethod
    def low(value: float) -> BaseAttribute:
        """
        "meter" attribute: low  
        High limit of low range  

        :param value: Valid floating-point number*  
        :return: An low attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("low", value)
            


    @staticmethod
    def max(value: float) -> BaseAttribute:
        """
        "meter" attribute: max  
        Upper bound of range  

        :param value: Valid floating-point number*  
        :return: An max attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("max", value)
            


    @staticmethod
    def min(value: float) -> BaseAttribute:
        """
        "meter" attribute: min  
        Lower bound of range  

        :param value: Valid floating-point number*  
        :return: An min attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("min", value)
            


    @staticmethod
    def optimum(value: float) -> BaseAttribute:
        """
        "meter" attribute: optimum  
        Optimum value in gauge  

        :param value: Valid floating-point number*  
        :return: An optimum attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("optimum", value)
            


    @staticmethod
    def value(value: float) -> BaseAttribute:
        """
        "meter" attribute: value  
        Current value of the element  

        :param value: Valid floating-point number  
        :return: An value attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("value", value)
            