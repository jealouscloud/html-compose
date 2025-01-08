from . import BaseAttribute
from typing import Literal, Union

class ScriptAttrs:
    """ 
    This module contains classes for attributes in the <script> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class async_(BaseAttribute):
        """
        script attribute: async
        Description: Execute script when available, without blocking while fetching
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("async", value)
            


    class blocking(BaseAttribute):
        """
        script attribute: blocking
        Description: Whether the element is potentially render-blocking
        Value: Unordered set of unique space-separated tokens*
        """
        
        def __init__(self, value):
            super().__init__("blocking", value)
            


    class crossorigin(BaseAttribute):
        """
        script attribute: crossorigin
        Description: How the element handles crossorigin requests
        Value: ['anonymous', 'use-credentials']
        """
        
        def __init__(self, value):
            super().__init__("crossorigin", value)
            


    class defer(BaseAttribute):
        """
        script attribute: defer
        Description: Defer script execution
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("defer", value)
            


    class fetchpriority(BaseAttribute):
        """
        script attribute: fetchpriority
        Description: Sets the priority for fetches initiated by the element
        Value: ['auto', 'high', 'low']
        """
        
        def __init__(self, value):
            super().__init__("fetchpriority", value)
            


    class integrity(BaseAttribute):
        """
        script attribute: integrity
        Description: Integrity metadata used in Subresource Integrity checks [SRI]
        Value: Text
        """
        
        def __init__(self, value: str):
            super().__init__("integrity", value)
            


    class nomodule(BaseAttribute):
        """
        script attribute: nomodule
        Description: Prevents execution in user agents that support module scripts
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("nomodule", value)
            


    class referrerpolicy(BaseAttribute):
        """
        script attribute: referrerpolicy
        Description: Referrer policy for fetches initiated by the element
        Value: Referrer policy
        """
        
        def __init__(self, value):
            super().__init__("referrerpolicy", value)
            


    class src(BaseAttribute):
        """
        script attribute: src
        Description: Address of the resource
        Value: Valid non-empty URL potentially surrounded by spaces
        """
        
        def __init__(self, value):
            super().__init__("src", value)
            


    class type(BaseAttribute):
        """
        script attribute: type
        Description: Type of script
        Value: "module"; a valid MIME type string that is not a JavaScript MIME type essence match
        """
        
        def __init__(self, value):
            super().__init__("type", value)
            