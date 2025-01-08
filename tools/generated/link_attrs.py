from . import BaseAttribute
from typing import Literal, Union

class LinkAttrs:
    """ 
    This module contains classes for attributes in the <link> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """ 
    
    class as_(BaseAttribute):
        """
        link attribute: as
        Description: Potential destination for a preload request (for rel="preload" and rel="modulepreload")
        Value: Potential destination, for rel="preload"; script-like destination, for rel="modulepreload"
        """
        
        def __init__(self, value):
            super().__init__("as", value)
            


    class blocking(BaseAttribute):
        """
        link attribute: blocking
        Description: Whether the element is potentially render-blocking
        Value: Unordered set of unique space-separated tokens*
        """
        
        def __init__(self, value):
            super().__init__("blocking", value)
            


    class color(BaseAttribute):
        """
        link attribute: color
        Description: Color to use when customizing a site's icon (for rel="mask-icon")
        Value: CSS <color>
        """
        
        def __init__(self, value):
            super().__init__("color", value)
            


    class crossorigin(BaseAttribute):
        """
        link attribute: crossorigin
        Description: How the element handles crossorigin requests
        Value: ['anonymous', 'use-credentials']
        """
        
        def __init__(self, value):
            super().__init__("crossorigin", value)
            


    class disabled(BaseAttribute):
        """
        link attribute: disabled
        Description: Whether the link is disabled
        Value: Boolean attribute
        """
        
        def __init__(self, value: bool):
            super().__init__("disabled", value)
            


    class fetchpriority(BaseAttribute):
        """
        link attribute: fetchpriority
        Description: Sets the priority for fetches initiated by the element
        Value: ['auto', 'high', 'low']
        """
        
        def __init__(self, value):
            super().__init__("fetchpriority", value)
            


    class href(BaseAttribute):
        """
        link attribute: href
        Description: Address of the hyperlink
        Value: Valid non-empty URL potentially surrounded by spaces
        """
        
        def __init__(self, value):
            super().__init__("href", value)
            


    class hreflang(BaseAttribute):
        """
        link attribute: hreflang
        Description: Language of the linked resource
        Value: Valid BCP 47 language tag
        """
        
        def __init__(self, value):
            super().__init__("hreflang", value)
            


    class imagesizes(BaseAttribute):
        """
        link attribute: imagesizes
        Description: Image sizes for different page layouts (for rel="preload")
        Value: Valid source size list
        """
        
        def __init__(self, value):
            super().__init__("imagesizes", value)
            


    class imagesrcset(BaseAttribute):
        """
        link attribute: imagesrcset
        Description: Images to use in different situations, e.g., high-resolution displays, small monitors, etc. (for rel="preload")
        Value: Comma-separated list of image candidate strings
        """
        
        def __init__(self, value):
            super().__init__("imagesrcset", value)
            


    class integrity(BaseAttribute):
        """
        link attribute: integrity
        Description: Integrity metadata used in Subresource Integrity checks [SRI]
        Value: Text
        """
        
        def __init__(self, value: str):
            super().__init__("integrity", value)
            


    class media(BaseAttribute):
        """
        link attribute: media
        Description: Applicable media
        Value: Valid media query list
        """
        
        def __init__(self, value):
            super().__init__("media", value)
            


    class referrerpolicy(BaseAttribute):
        """
        link attribute: referrerpolicy
        Description: Referrer policy for fetches initiated by the element
        Value: Referrer policy
        """
        
        def __init__(self, value):
            super().__init__("referrerpolicy", value)
            


    class rel(BaseAttribute):
        """
        link attribute: rel
        Description: Relationship between the document containing the hyperlink and the destination resource
        Value: Unordered set of unique space-separated tokens*
        """
        
        def __init__(self, value):
            super().__init__("rel", value)
            


    class sizes(BaseAttribute):
        """
        link attribute: sizes
        Description: Sizes of the icons (for rel="icon")
        Value: Unordered set of unique space-separated tokens, ASCII case-insensitive, consisting of sizes*
        """
        
        def __init__(self, value):
            super().__init__("sizes", value)
            


    class title(BaseAttribute):
        """
        link attribute: title
        Description: Title of the link  OR  CSS style sheet set name
        Value: Text  OR  Text
        """
        
        def __init__(self, value):
            super().__init__("title", value)
            


    class type(BaseAttribute):
        """
        link attribute: type
        Description: Hint for the type of the referenced resource
        Value: Valid MIME type string
        """
        
        def __init__(self, value):
            super().__init__("type", value)
            