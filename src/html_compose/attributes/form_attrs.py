from . import BaseAttribute


class FormAttrs:
    """
    This module contains classes for attributes in the <form> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class accept_charset(BaseAttribute):
        """
        form attribute: accept-charset
        Description: Character encodings to use for form submission
        Value: ASCII case-insensitive match for "UTF-8"
        """

        def __init__(self, value):
            super().__init__("accept-charset", value)

    class action(BaseAttribute):
        """
        form attribute: action
        Description: URL to use for form submission
        Value: Valid non-empty URL potentially surrounded by spaces
        """

        def __init__(self, value):
            super().__init__("action", value)

    class autocomplete(BaseAttribute):
        """
        form attribute: autocomplete
        Description: Default setting for autofill feature for controls in the form
        Value: ['on', 'off']
        """

        def __init__(self, value):
            super().__init__("autocomplete", value)

    class enctype(BaseAttribute):
        """
        form attribute: enctype
        Description: Entry list encoding type to use for form submission
        Value: ['application/x-www-form-urlencoded', 'multipart/form-data', 'text/plain']
        """

        def __init__(self, value):
            super().__init__("enctype", value)

    class method(BaseAttribute):
        """
        form attribute: method
        Description: Variant to use for form submission
        Value: ['GET', 'POST', 'dialog']
        """

        def __init__(self, value):
            super().__init__("method", value)

    class name(BaseAttribute):
        """
        form attribute: name
        Description: Name of form to use in the document.forms API
        Value: Text*
        """

        def __init__(self, value: str):
            super().__init__("name", value)

    class novalidate(BaseAttribute):
        """
        form attribute: novalidate
        Description: Bypass form control validation for form submission
        Value: Boolean attribute
        """

        def __init__(self, value: bool):
            super().__init__("novalidate", value)

    class target(BaseAttribute):
        """
        form attribute: target
        Description: Navigable for form submission
        Value: Valid navigable target name or keyword
        """

        def __init__(self, value):
            super().__init__("target", value)
