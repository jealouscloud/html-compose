from . import BaseAttribute
from typing import Literal, Union

class ImgAttrs:
    """ 
    This module contains classes for attributes in the <img> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class alt(BaseAttribute):
        """
        img attribute: alt
        Description: Replacement text for use when images are not available
        Value: Text*
        """
        
        def __init__(self, value: str):
            super().__init__("alt", value)
            


    class crossorigin(BaseAttribute):
        """
        img attribute: crossorigin
        Description: How the element handles crossorigin requests
        Value: ['anonymous', 'use-credentials']
        """
        
        def __init__(self, value):
            super().__init__("crossorigin", value)
            


    class decoding(BaseAttribute):
        """
        img attribute: decoding
        Description: Decoding hint to use when processing this image for presentation
        Value: ['sync', 'async', 'auto']
        """
        
        def __init__(self, value):
            super().__init__("decoding", value)
            


    class fetchpriority(BaseAttribute):
        """
        img attribute: fetchpriority
        Description: Sets the priority for fetches initiated by the element
        Value: ['auto', 'high', 'low']
        """
        
        def __init__(self, value):
            super().__init__("fetchpriority", value)
            


    class height(BaseAttribute):
        """
        img attribute: height
        Description: Vertical dimension
        Value: Valid non-negative integer
        """
        
        def __init__(self, value: int):
            super().__init__("height", value)
            


    class ismap(BaseAttribute):
        """
        img attribute: ismap
        Description: Whether the image is a server-side image map
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("ismap", value)
            


    class loading(BaseAttribute):
        """
        img attribute: loading
        Description: Used when determining loading deferral
        Value: ['lazy', 'eager']
        """
        
        def __init__(self, value):
            super().__init__("loading", value)
            


    class referrerpolicy(BaseAttribute):
        """
        img attribute: referrerpolicy
        Description: Referrer policy for fetches initiated by the element
        Value: Referrer policy
        """
        
        def __init__(self, value):
            super().__init__("referrerpolicy", value)
            


    class sizes(BaseAttribute):
        """
        img attribute: sizes
        Description: Image sizes for different page layouts
        Value: Valid source size list
        """
        
        def __init__(self, value):
            super().__init__("sizes", value)
            


    class src(BaseAttribute):
        """
        img attribute: src
        Description: Address of the resource
        Value: Valid non-empty URL potentially surrounded by spaces
        """
        
        def __init__(self, value):
            super().__init__("src", value)
            


    class srcset(BaseAttribute):
        """
        img attribute: srcset
        Description: Images to use in different situations, e.g., high-resolution displays, small monitors, etc.
        Value: Comma-separated list of image candidate strings
        """
        
        def __init__(self, value):
            super().__init__("srcset", value)
            


    class usemap(BaseAttribute):
        """
        img attribute: usemap
        Description: Name of image map to use
        Value: Valid hash-name reference*
        """
        
        def __init__(self, value):
            super().__init__("usemap", value)
            


    class width(BaseAttribute):
        """
        img attribute: width
        Description: Horizontal dimension
        Value: Valid non-negative integer
        """
        
        def __init__(self, value: int):
            super().__init__("width", value)
            