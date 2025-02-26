from . import BaseAttribute


class TextareaAttrs:
    """
    This module contains classes for attributes in the <textarea> element.
    Which is inherited by the element so the element can be a reference to our attributes
    """

    class autocomplete(BaseAttribute):
        """
        textarea attribute: autocomplete
        Description: Hint for form autofill feature
        Value: Autofill field name and related tokens*
        """

        def __init__(self, value):
            super().__init__("autocomplete", value)

    class cols(BaseAttribute):
        """
        textarea attribute: cols
        Description: Maximum number of characters per line
        Value: Valid non-negative integer greater than zero
        """

        def __init__(self, value):
            super().__init__("cols", value)

    class dirname(BaseAttribute):
        """
        textarea attribute: dirname
        Description: Name of form control to use for sending the element's directionality in form submission
        Value: Text*
        """

        def __init__(self, value: str):
            super().__init__("dirname", value)

    class disabled(BaseAttribute):
        """
        textarea attribute: disabled
        Description: Whether the form control is disabled
        Value: Boolean attribute
        """

        def __init__(self, value: bool):
            super().__init__("disabled", value)

    class form(BaseAttribute):
        """
        textarea attribute: form
        Description: Associates the element with a form element
        Value: ID*
        """

        def __init__(self, value):
            super().__init__("form", value)

    class maxlength(BaseAttribute):
        """
        textarea attribute: maxlength
        Description: Maximum length of value
        Value: Valid non-negative integer
        """

        def __init__(self, value: int):
            super().__init__("maxlength", value)

    class minlength(BaseAttribute):
        """
        textarea attribute: minlength
        Description: Minimum length of value
        Value: Valid non-negative integer
        """

        def __init__(self, value: int):
            super().__init__("minlength", value)

    class name(BaseAttribute):
        """
        textarea attribute: name
        Description: Name of the element to use for form submission and in the form.elements API
        Value: Text*
        """

        def __init__(self, value: str):
            super().__init__("name", value)

    class placeholder(BaseAttribute):
        """
        textarea attribute: placeholder
        Description: User-visible label to be placed within the form control
        Value: Text*
        """

        def __init__(self, value: str):
            super().__init__("placeholder", value)

    class readonly(BaseAttribute):
        """
        textarea attribute: readonly
        Description: Whether to allow the value to be edited by the user
        Value: Boolean attribute
        """

        def __init__(self, value: bool):
            super().__init__("readonly", value)

    class required(BaseAttribute):
        """
        textarea attribute: required
        Description: Whether the control is required for form submission
        Value: Boolean attribute
        """

        def __init__(self, value: bool):
            super().__init__("required", value)

    class rows(BaseAttribute):
        """
        textarea attribute: rows
        Description: Number of lines to show
        Value: Valid non-negative integer greater than zero
        """

        def __init__(self, value):
            super().__init__("rows", value)

    class wrap(BaseAttribute):
        """
        textarea attribute: wrap
        Description: How the value of the form control is to be wrapped for form submission
        Value: ['soft', 'hard']
        """

        def __init__(self, value):
            super().__init__("wrap", value)
