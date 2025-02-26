from . import BaseAttribute


class InputAttrs:
    """
    This module contains classes for attributes in the <input> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class accept(BaseAttribute):
        """
        input attribute: accept
        Description: Hint for expected file type in file upload controls
        Value: Set of comma-separated tokens* consisting of valid MIME type strings with no parameters or audio/*, video/*, or image/*
        """

        def __init__(self, value):
            super().__init__("accept", value)

    class alpha(BaseAttribute):
        """
        input attribute: alpha
        Description: Allow the color's alpha component to be set
        Value: Boolean attribute
        """

        def __init__(self, value: bool):
            super().__init__("alpha", value)

    class alt(BaseAttribute):
        """
        input attribute: alt
        Description: Replacement text for use when images are not available
        Value: Text*
        """

        def __init__(self, value: str):
            super().__init__("alt", value)

    class autocomplete(BaseAttribute):
        """
        input attribute: autocomplete
        Description: Hint for form autofill feature
        Value: Autofill field name and related tokens*
        """

        def __init__(self, value):
            super().__init__("autocomplete", value)

    class checked(BaseAttribute):
        """
        input attribute: checked
        Description: Whether the control is checked
        Value: Boolean attribute
        """

        def __init__(self, value: bool):
            super().__init__("checked", value)

    class colorspace(BaseAttribute):
        """
        input attribute: colorspace
        Description: The color space of the serialized color
        Value: ['limited-srgb', 'display-p3']
        """

        def __init__(self, value):
            super().__init__("colorspace", value)

    class dirname(BaseAttribute):
        """
        input attribute: dirname
        Description: Name of form control to use for sending the element's directionality in form submission
        Value: Text*
        """

        def __init__(self, value: str):
            super().__init__("dirname", value)

    class disabled(BaseAttribute):
        """
        input attribute: disabled
        Description: Whether the form control is disabled
        Value: Boolean attribute
        """

        def __init__(self, value: bool):
            super().__init__("disabled", value)

    class form(BaseAttribute):
        """
        input attribute: form
        Description: Associates the element with a form element
        Value: ID*
        """

        def __init__(self, value):
            super().__init__("form", value)

    class formaction(BaseAttribute):
        """
        input attribute: formaction
        Description: URL to use for form submission
        Value: Valid non-empty URL potentially surrounded by spaces
        """

        def __init__(self, value):
            super().__init__("formaction", value)

    class formenctype(BaseAttribute):
        """
        input attribute: formenctype
        Description: Entry list encoding type to use for form submission
        Value: ['application/x-www-form-urlencoded', 'multipart/form-data', 'text/plain']
        """

        def __init__(self, value):
            super().__init__("formenctype", value)

    class formmethod(BaseAttribute):
        """
        input attribute: formmethod
        Description: Variant to use for form submission
        Value: ['GET', 'POST', 'dialog']
        """

        def __init__(self, value):
            super().__init__("formmethod", value)

    class formnovalidate(BaseAttribute):
        """
        input attribute: formnovalidate
        Description: Bypass form control validation for form submission
        Value: Boolean attribute
        """

        def __init__(self, value: bool):
            super().__init__("formnovalidate", value)

    class formtarget(BaseAttribute):
        """
        input attribute: formtarget
        Description: Navigable for form submission
        Value: Valid navigable target name or keyword
        """

        def __init__(self, value):
            super().__init__("formtarget", value)

    class height(BaseAttribute):
        """
        input attribute: height
        Description: Vertical dimension
        Value: Valid non-negative integer
        """

        def __init__(self, value: int):
            super().__init__("height", value)

    class list(BaseAttribute):
        """
        input attribute: list
        Description: List of autocomplete options
        Value: ID*
        """

        def __init__(self, value):
            super().__init__("list", value)

    class max(BaseAttribute):
        """
        input attribute: max
        Description: Maximum value
        Value: Varies*
        """

        def __init__(self, value):
            super().__init__("max", value)

    class maxlength(BaseAttribute):
        """
        input attribute: maxlength
        Description: Maximum length of value
        Value: Valid non-negative integer
        """

        def __init__(self, value: int):
            super().__init__("maxlength", value)

    class min(BaseAttribute):
        """
        input attribute: min
        Description: Minimum value
        Value: Varies*
        """

        def __init__(self, value):
            super().__init__("min", value)

    class minlength(BaseAttribute):
        """
        input attribute: minlength
        Description: Minimum length of value
        Value: Valid non-negative integer
        """

        def __init__(self, value: int):
            super().__init__("minlength", value)

    class multiple(BaseAttribute):
        """
        input attribute: multiple
        Description: Whether to allow multiple values
        Value: Boolean attribute
        """

        def __init__(self, value: bool):
            super().__init__("multiple", value)

    class name(BaseAttribute):
        """
        input attribute: name
        Description: Name of the element to use for form submission and in the form.elements API
        Value: Text*
        """

        def __init__(self, value: str):
            super().__init__("name", value)

    class pattern(BaseAttribute):
        """
        input attribute: pattern
        Description: Pattern to be matched by the form control's value
        Value: Regular expression matching the JavaScript Pattern production
        """

        def __init__(self, value):
            super().__init__("pattern", value)

    class placeholder(BaseAttribute):
        """
        input attribute: placeholder
        Description: User-visible label to be placed within the form control
        Value: Text*
        """

        def __init__(self, value: str):
            super().__init__("placeholder", value)

    class popovertarget(BaseAttribute):
        """
        input attribute: popovertarget
        Description: Targets a popover element to toggle, show, or hide
        Value: ID*
        """

        def __init__(self, value):
            super().__init__("popovertarget", value)

    class popovertargetaction(BaseAttribute):
        """
        input attribute: popovertargetaction
        Description: Indicates whether a targeted popover element is to be toggled, shown, or hidden
        Value: ['toggle', 'show', 'hide']
        """

        def __init__(self, value):
            super().__init__("popovertargetaction", value)

    class readonly(BaseAttribute):
        """
        input attribute: readonly
        Description: Whether to allow the value to be edited by the user
        Value: Boolean attribute
        """

        def __init__(self, value: bool):
            super().__init__("readonly", value)

    class required(BaseAttribute):
        """
        input attribute: required
        Description: Whether the control is required for form submission
        Value: Boolean attribute
        """

        def __init__(self, value: bool):
            super().__init__("required", value)

    class size(BaseAttribute):
        """
        input attribute: size
        Description: Size of the control
        Value: Valid non-negative integer greater than zero
        """

        def __init__(self, value):
            super().__init__("size", value)

    class src(BaseAttribute):
        """
        input attribute: src
        Description: Address of the resource
        Value: Valid non-empty URL potentially surrounded by spaces
        """

        def __init__(self, value):
            super().__init__("src", value)

    class step(BaseAttribute):
        """
        input attribute: step
        Description: Granularity to be matched by the form control's value
        Value: Valid floating-point number greater than zero, or "any"
        """

        def __init__(self, value: float):
            super().__init__("step", value)

    class title(BaseAttribute):
        """
        input attribute: title
        Description: Description of pattern (when used with pattern attribute)
        Value: Text
        """

        def __init__(self, value: str):
            super().__init__("title", value)

    class type(BaseAttribute):
        """
        input attribute: type
        Description: Type of form control
        Value: input type keyword
        """

        def __init__(self, value):
            super().__init__("type", value)

    class value(BaseAttribute):
        """
        input attribute: value
        Description: Value of the form control
        Value: Varies*
        """

        def __init__(self, value):
            super().__init__("value", value)

    class width(BaseAttribute):
        """
        input attribute: width
        Description: Horizontal dimension
        Value: Valid non-negative integer
        """

        def __init__(self, value: int):
            super().__init__("width", value)
