from . import BaseAttribute
from typing import Literal, Iterable, Mapping
from ..base_types import Resolvable, StrLike

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

        Args:
            value:
                Boolean attribute
        
        Returns:
            An async attribute to be added to your element

        """
        
        return BaseAttribute("async", value)
            


    @staticmethod
    def blocking(value: Resolvable) -> BaseAttribute:
        """
        "script" attribute: blocking  
        Whether the element is potentially render-blocking  

        Args:
            value:
                Unordered set of unique space-separated tokens*
        
        Returns:
            An blocking attribute to be added to your element

        """
        
        return BaseAttribute("blocking", value)
            


    @staticmethod
    def crossorigin(value: Literal['anonymous', 'use-credentials']) -> BaseAttribute:
        """
        "script" attribute: crossorigin  
        How the element handles crossorigin requests  

        Args:
            value:
                ['anonymous', 'use-credentials']
        
        Returns:
            An crossorigin attribute to be added to your element

        """
        
        return BaseAttribute("crossorigin", value)
            


    @staticmethod
    def defer(value: bool) -> BaseAttribute:
        """
        "script" attribute: defer  
        Defer script execution  

        Args:
            value:
                Boolean attribute
        
        Returns:
            An defer attribute to be added to your element

        """
        
        return BaseAttribute("defer", value)
            


    @staticmethod
    def fetchpriority(value: Literal['auto', 'high', 'low']) -> BaseAttribute:
        """
        "script" attribute: fetchpriority  
        Sets the priority for fetches initiated by the element  

        Args:
            value:
                ['auto', 'high', 'low']
        
        Returns:
            An fetchpriority attribute to be added to your element

        """
        
        return BaseAttribute("fetchpriority", value)
            


    @staticmethod
    def integrity(value: StrLike) -> BaseAttribute:
        """
        "script" attribute: integrity  
        Integrity metadata used in Subresource Integrity checks [SRI]  

        Args:
            value:
                Text
        
        Returns:
            An integrity attribute to be added to your element

        """
        
        return BaseAttribute("integrity", value)
            


    @staticmethod
    def nomodule(value: bool) -> BaseAttribute:
        """
        "script" attribute: nomodule  
        Prevents execution in user agents that support module scripts  

        Args:
            value:
                Boolean attribute
        
        Returns:
            An nomodule attribute to be added to your element

        """
        
        return BaseAttribute("nomodule", value)
            


    @staticmethod
    def referrerpolicy(value) -> BaseAttribute:
        """
        "script" attribute: referrerpolicy  
        Referrer policy for fetches initiated by the element  

        Args:
            value:
                Referrer policy
        
        Returns:
            An referrerpolicy attribute to be added to your element

        """
        
        return BaseAttribute("referrerpolicy", value)
            


    @staticmethod
    def src(value) -> BaseAttribute:
        """
        "script" attribute: src  
        Address of the resource  

        Args:
            value:
                Valid non-empty URL potentially surrounded by spaces
        
        Returns:
            An src attribute to be added to your element

        """
        
        return BaseAttribute("src", value)
            


    @staticmethod
    def type(value) -> BaseAttribute:
        """
        "script" attribute: type  
        Type of script  

        Args:
            value:
                "module"; a valid MIME type string that is not a JavaScript MIME type essence match
        
        Returns:
            An type attribute to be added to your element

        """
        
        return BaseAttribute("type", value)
            