from . import BaseAttribute
from typing import Literal
from ..base_types import StrLike


class InputAttrs:
    """
    This module contains functions for attributes in the 'input' element.
    Which is inherited by a class so we can generate type hints
    """

    @staticmethod
    def accept(value) -> BaseAttribute:
        """
        "input" attribute: accept
        Hint for expected file type in file upload controls

        Args:
            value:
                Set of comma-separated tokens* consisting of valid MIME type strings with no parameters or audio/*, video/*, or image/*

        Returns:
            An accept attribute to be added to your element

        """

        return BaseAttribute("accept", value)

    @staticmethod
    def alpha(value: bool) -> BaseAttribute:
        """
        "input" attribute: alpha
        Allow the color's alpha component to be set

        Args:
            value:
                Boolean attribute

        Returns:
            An alpha attribute to be added to your element

        """

        return BaseAttribute("alpha", value)

    @staticmethod
    def alt(value: StrLike) -> BaseAttribute:
        """
        "input" attribute: alt
        Replacement text for use when images are not available

        Args:
            value:
                Text*

        Returns:
            An alt attribute to be added to your element

        """

        return BaseAttribute("alt", value)

    @staticmethod
    def autocomplete(value) -> BaseAttribute:
        """
        "input" attribute: autocomplete
        Hint for form autofill feature

        Args:
            value:
                Autofill field name and related tokens*

        Returns:
            An autocomplete attribute to be added to your element

        """

        return BaseAttribute("autocomplete", value)

    @staticmethod
    def checked(value: bool) -> BaseAttribute:
        """
        "input" attribute: checked
        Whether the control is checked

        Args:
            value:
                Boolean attribute

        Returns:
            An checked attribute to be added to your element

        """

        return BaseAttribute("checked", value)

    @staticmethod
    def colorspace(
        value: Literal["limited-srgb", "display-p3"],
    ) -> BaseAttribute:
        """
        "input" attribute: colorspace
        The color space of the serialized color

        Args:
            value:
                ['limited-srgb', 'display-p3']

        Returns:
            An colorspace attribute to be added to your element

        """

        return BaseAttribute("colorspace", value)

    @staticmethod
    def dirname(value: StrLike) -> BaseAttribute:
        """
        "input" attribute: dirname
        Name of form control to use for sending the element's directionality in form submission

        Args:
            value:
                Text*

        Returns:
            An dirname attribute to be added to your element

        """

        return BaseAttribute("dirname", value)

    @staticmethod
    def disabled(value: bool) -> BaseAttribute:
        """
        "input" attribute: disabled
        Whether the form control is disabled

        Args:
            value:
                Boolean attribute

        Returns:
            An disabled attribute to be added to your element

        """

        return BaseAttribute("disabled", value)

    @staticmethod
    def form(value) -> BaseAttribute:
        """
        "input" attribute: form
        Associates the element with a form element

        Args:
            value:
                ID*

        Returns:
            An form attribute to be added to your element

        """

        return BaseAttribute("form", value)

    @staticmethod
    def formaction(value) -> BaseAttribute:
        """
        "input" attribute: formaction
        URL to use for form submission

        Args:
            value:
                Valid non-empty URL potentially surrounded by spaces

        Returns:
            An formaction attribute to be added to your element

        """

        return BaseAttribute("formaction", value)

    @staticmethod
    def formenctype(
        value: Literal[
            "application/x-www-form-urlencoded",
            "multipart/form-data",
            "text/plain",
        ],
    ) -> BaseAttribute:
        """
        "input" attribute: formenctype
        Entry list encoding type to use for form submission

        Args:
            value:
                ['application/x-www-form-urlencoded', 'multipart/form-data', 'text/plain']

        Returns:
            An formenctype attribute to be added to your element

        """

        return BaseAttribute("formenctype", value)

    @staticmethod
    def formmethod(value: Literal["GET", "POST", "dialog"]) -> BaseAttribute:
        """
        "input" attribute: formmethod
        Variant to use for form submission

        Args:
            value:
                ['GET', 'POST', 'dialog']

        Returns:
            An formmethod attribute to be added to your element

        """

        return BaseAttribute("formmethod", value)

    @staticmethod
    def formnovalidate(value: bool) -> BaseAttribute:
        """
        "input" attribute: formnovalidate
        Bypass form control validation for form submission

        Args:
            value:
                Boolean attribute

        Returns:
            An formnovalidate attribute to be added to your element

        """

        return BaseAttribute("formnovalidate", value)

    @staticmethod
    def formtarget(value) -> BaseAttribute:
        """
        "input" attribute: formtarget
        Navigable for form submission

        Args:
            value:
                Valid navigable target name or keyword

        Returns:
            An formtarget attribute to be added to your element

        """

        return BaseAttribute("formtarget", value)

    @staticmethod
    def height(value: int) -> BaseAttribute:
        """
        "input" attribute: height
        Vertical dimension

        Args:
            value:
                Valid non-negative integer

        Returns:
            An height attribute to be added to your element

        """

        return BaseAttribute("height", value)

    @staticmethod
    def list(value) -> BaseAttribute:
        """
        "input" attribute: list
        List of autocomplete options

        Args:
            value:
                ID*

        Returns:
            An list attribute to be added to your element

        """

        return BaseAttribute("list", value)

    @staticmethod
    def max(value) -> BaseAttribute:
        """
        "input" attribute: max
        Maximum value

        Args:
            value:
                Varies*

        Returns:
            An max attribute to be added to your element

        """

        return BaseAttribute("max", value)

    @staticmethod
    def maxlength(value: int) -> BaseAttribute:
        """
        "input" attribute: maxlength
        Maximum length of value

        Args:
            value:
                Valid non-negative integer

        Returns:
            An maxlength attribute to be added to your element

        """

        return BaseAttribute("maxlength", value)

    @staticmethod
    def min(value) -> BaseAttribute:
        """
        "input" attribute: min
        Minimum value

        Args:
            value:
                Varies*

        Returns:
            An min attribute to be added to your element

        """

        return BaseAttribute("min", value)

    @staticmethod
    def minlength(value: int) -> BaseAttribute:
        """
        "input" attribute: minlength
        Minimum length of value

        Args:
            value:
                Valid non-negative integer

        Returns:
            An minlength attribute to be added to your element

        """

        return BaseAttribute("minlength", value)

    @staticmethod
    def multiple(value: bool) -> BaseAttribute:
        """
        "input" attribute: multiple
        Whether to allow multiple values

        Args:
            value:
                Boolean attribute

        Returns:
            An multiple attribute to be added to your element

        """

        return BaseAttribute("multiple", value)

    @staticmethod
    def name(value: StrLike) -> BaseAttribute:
        """
        "input" attribute: name
        Name of the element to use for form submission and in the form.elements API

        Args:
            value:
                Text*

        Returns:
            An name attribute to be added to your element

        """

        return BaseAttribute("name", value)

    @staticmethod
    def pattern(value) -> BaseAttribute:
        """
        "input" attribute: pattern
        Pattern to be matched by the form control's value

        Args:
            value:
                Regular expression matching the JavaScript Pattern production

        Returns:
            An pattern attribute to be added to your element

        """

        return BaseAttribute("pattern", value)

    @staticmethod
    def placeholder(value: StrLike) -> BaseAttribute:
        """
        "input" attribute: placeholder
        User-visible label to be placed within the form control

        Args:
            value:
                Text*

        Returns:
            An placeholder attribute to be added to your element

        """

        return BaseAttribute("placeholder", value)

    @staticmethod
    def popovertarget(value) -> BaseAttribute:
        """
        "input" attribute: popovertarget
        Targets a popover element to toggle, show, or hide

        Args:
            value:
                ID*

        Returns:
            An popovertarget attribute to be added to your element

        """

        return BaseAttribute("popovertarget", value)

    @staticmethod
    def popovertargetaction(
        value: Literal["toggle", "show", "hide"],
    ) -> BaseAttribute:
        """
        "input" attribute: popovertargetaction
        Indicates whether a targeted popover element is to be toggled, shown, or hidden

        Args:
            value:
                ['toggle', 'show', 'hide']

        Returns:
            An popovertargetaction attribute to be added to your element

        """

        return BaseAttribute("popovertargetaction", value)

    @staticmethod
    def readonly(value: bool) -> BaseAttribute:
        """
        "input" attribute: readonly
        Whether to allow the value to be edited by the user

        Args:
            value:
                Boolean attribute

        Returns:
            An readonly attribute to be added to your element

        """

        return BaseAttribute("readonly", value)

    @staticmethod
    def required(value: bool) -> BaseAttribute:
        """
        "input" attribute: required
        Whether the control is required for form submission

        Args:
            value:
                Boolean attribute

        Returns:
            An required attribute to be added to your element

        """

        return BaseAttribute("required", value)

    @staticmethod
    def size(value) -> BaseAttribute:
        """
        "input" attribute: size
        Size of the control

        Args:
            value:
                Valid non-negative integer greater than zero

        Returns:
            An size attribute to be added to your element

        """

        return BaseAttribute("size", value)

    @staticmethod
    def src(value) -> BaseAttribute:
        """
        "input" attribute: src
        Address of the resource

        Args:
            value:
                Valid non-empty URL potentially surrounded by spaces

        Returns:
            An src attribute to be added to your element

        """

        return BaseAttribute("src", value)

    @staticmethod
    def step(value: float) -> BaseAttribute:
        """
        "input" attribute: step
        Granularity to be matched by the form control's value

        Args:
            value:
                Valid floating-point number greater than zero, or "any"

        Returns:
            An step attribute to be added to your element

        """

        return BaseAttribute("step", value)

    @staticmethod
    def title(value: StrLike) -> BaseAttribute:
        """
        "input" attribute: title
        Description of pattern (when used with pattern attribute)

        Args:
            value:
                Text

        Returns:
            An title attribute to be added to your element

        """

        return BaseAttribute("title", value)

    @staticmethod
    def type(value) -> BaseAttribute:
        """
        "input" attribute: type
        Type of form control

        Args:
            value:
                input type keyword

        Returns:
            An type attribute to be added to your element

        """

        return BaseAttribute("type", value)

    @staticmethod
    def value(value) -> BaseAttribute:
        """
        "input" attribute: value
        Value of the form control

        Args:
            value:
                Varies*

        Returns:
            An value attribute to be added to your element

        """

        return BaseAttribute("value", value)

    @staticmethod
    def width(value: int) -> BaseAttribute:
        """
        "input" attribute: width
        Horizontal dimension

        Args:
            value:
                Valid non-negative integer

        Returns:
            An width attribute to be added to your element

        """

        return BaseAttribute("width", value)
