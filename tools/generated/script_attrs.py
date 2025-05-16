from . import BaseAttribute
from typing import Literal, Union

class ScriptAttrs:
    """ 
    This module contains functions for attributes in the 'script' element.
    Which is inherited by a class so we can generate type hints
    """ 
    
    @staticmethod
    def async_(value: bool) -> BaseAttribute:
        """
        "script" attribute: async  
        Execute script when available, without blocking while fetching  

        :param value: Boolean attribute  
        :return: An async attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("async", value)
            


    @staticmethod
    def blocking(value: list) -> BaseAttribute:
        """
        "script" attribute: blocking  
        Whether the element is potentially render-blocking  

        :param value: Unordered set of unique space-separated tokens*  
        :return: An blocking attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("blocking", value)
            


    @staticmethod
    def crossorigin(value: Literal['anonymous', 'use-credentials']) -> BaseAttribute:
        """
        "script" attribute: crossorigin  
        How the element handles crossorigin requests  

        :param value: ['anonymous', 'use-credentials']  
        :return: An crossorigin attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("crossorigin", value)
            


    @staticmethod
    def defer(value: bool) -> BaseAttribute:
        """
        "script" attribute: defer  
        Defer script execution  

        :param value: Boolean attribute  
        :return: An defer attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("defer", value)
            


    @staticmethod
    def fetchpriority(value: Literal['auto', 'high', 'low']) -> BaseAttribute:
        """
        "script" attribute: fetchpriority  
        Sets the priority for fetches initiated by the element  

        :param value: ['auto', 'high', 'low']  
        :return: An fetchpriority attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("fetchpriority", value)
            


    @staticmethod
    def integrity(value: str) -> BaseAttribute:
        """
        "script" attribute: integrity  
        Integrity metadata used in Subresource Integrity checks [SRI]  

        :param value: Text  
        :return: An integrity attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("integrity", value)
            


    @staticmethod
    def nomodule(value: bool) -> BaseAttribute:
        """
        "script" attribute: nomodule  
        Prevents execution in user agents that support module scripts  

        :param value: Boolean attribute  
        :return: An nomodule attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("nomodule", value)
            


    @staticmethod
    def referrerpolicy(value) -> BaseAttribute:
        """
        "script" attribute: referrerpolicy  
        Referrer policy for fetches initiated by the element  

        :param value: Referrer policy  
        :return: An referrerpolicy attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("referrerpolicy", value)
            


    @staticmethod
    def src(value) -> BaseAttribute:
        """
        "script" attribute: src  
        Address of the resource  

        :param value: Valid non-empty URL potentially surrounded by spaces  
        :return: An src attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("src", value)
            


    @staticmethod
    def type(value) -> BaseAttribute:
        """
        "script" attribute: type  
        Type of script  

        :param value: "module"; a valid MIME type string that is not a JavaScript MIME type essence match  
        :return: An type attribute to be added to your element
        """ # fmt: skip
        
        return BaseAttribute("type", value)
            