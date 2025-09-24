# Attributes
The goal of the library is to enable the user to make design choices
about how they generate their HTML.

Therefore, the library proposes several ways to define attributes for an 
HTML element.

The theory is that creating the least resistance to a successful pattern makes way
for its adoption.

```python
from html_compose import div
is_error = False

# keyword arg syntax (preferred)
# note that attributes that conflict with Python keywords
# have an underscore_ appended. This was chosen so autocomplete still works.

div(class_="flex")
div(class_=["flex", "items-center"])
div(class_={
    "flex": True,
    "error": is_error
})
div([div.hint.class_("flex")])

div([div._.class_("flex")])
# div._ is a syntax shorthand for div.hint

# attrs dict syntax
div(attrs={"class": "flex"})
div(attrs={"class": ["flex"]})
div(attrs={"class": {
    "flex": True,
    "error": is_error
}})

# Also technically works
div(attrs={"class": div.hint.class_("flex")})

# attrs list syntax
div(attrs=[div.hint.class_("flex")])
div(attrs=[div.hint.class_(["flex", "items-center"])])
div(attrs=[div.hint.class_({
    "flex": True,
    "error": is_error == True
})])

# Combining the two:
div(attrs=[div.hint.class_("flex")], tabindex=1)
```

## BaseAttribute
All attributes inherit from `BaseAttribute`, which defines a key and a value and resolves at render time.

The `class` and `style` attributes have special rules to join values with their correct delimiter.

```python
from html_compose import div
is_red = False
# dict of str:bool - if the value is true, the key is rendered as part of the class list
# truthy = rendered
# falsey = ignored

div.hint.class_({
        'red': is_red,
        'blue': not is_red
    }
)
# "blue"

# list of values (joined by whitespace)
div.hint.class_(["red", "center"])
# "red center"

div._.class_("red")
# "red"
```

## `attrs=` parameter syntax

In the constructor for any element, you can specify the `attrs` parameter.

It can be either a list or a dictionary.

### Implicit/positional `attrs` argument
Although the documentation is explicit in using the `attrs` kwarg, `attrs` is
actually the first argument of the constructor and its name can be omitted.
```python
div({"class": "flex"})
```
Instead of 
```python
div(attrs={"class": "flex"})
```

### list
It supports a list of BaseAttributes but also you can mix a dictionary in as well.

```python
from html_compose.elements import a, div

div(attrs=[div.class_("red")])

a(attrs=[
    a.hint.href("https://google.com"),
    a.hint.tabindex(1),
    a.hint.class_(["flex", "flex-col"])
])


a(attrs=[
    {"@custom": "value"},
    a.hint.href("https://google.com"),
    a.hint.tabindex(1),
    a.hint.class_(["flex", "flex-col"])
])

# string / list of string is explicitly NOT supported
# it requires disabling sanitization and is therefore quietly prone to XSS
div(attrs=['class="red"']) # ❌
```

### dict

```python
a(attrs={
    "href": "https://google.com"),
    "tabindex": 1
})

div(attrs={
    "class": "red"
})



div(attrs={
    "class": ["flex", "items-center"]
})
```

## Keyword argument extension
An extension of the `attrs` syntax was generated for all built-in HTML elements. It would be time-consuming to do this for custom element types, but code generation lends itself well to this case.

Traditionally, kwargs would be too non-descript to provide helpful editor hints.

To aid with fluent document writing, each element was generated with its attributes as parameters and a paired docstring.
i.e.
`:param href: Address of the hyperlink`

```python
a(href="https://google.com", tabindex=1)
```

Under the hood, it's all translated to the `BaseAttribute` class, and the value is
escaped before rendering.

# Breakdown

There are a number of options for declaring an attribute value, which are shown above. 
The basic idea is 


`attrs`, the first parameter, is a key,value attribute set, or a list 
containing one or more of
  * a `dict` that translates `key="{safe_text(value)}"`, as if attrs were a dict
  * `BaseAttribute` which may be from a hint class for an element or library

## Attribute definitions
Care was put into generating attribute definitions for each class.

Anything found in the HTML specification document is available in an element's cousin attribute class.

i.e. the `img` class has a cousin class `ImgAttrs`.

We can access the definition of an attribute for that element via `ImgAttrs.$attr` i.e. `ImgAttrs.alt(value="demo")`. Each element, like `img`, has a child class `hint` which inherits from its sibling attrs class (`ImgAttrs`), so you can access the same definition via `img.hint.alt("...")`. 

Additionally, there's a `_` shorthand for `img.hint`. `img._` is just a reference to `img.hint`.

The purpose of this system is to provide full type hints.

It also serves as an example for extensions to add attribute sets under their
own namespaces/classes.

## Extensions

Quality extensions are recommended to work with your chosen tech stack.
The idea is to give you guardrails and documentation directly in your IDE.

```python
from html_compose.base_attribute import BaseAttribute
from html_compose import button
class htmx:
    '''
    Attributes for the HTMX framework.
    '''

    @staticmethod
    def hx_get(value: str) -> BaseAttribute:
        '''
        htmx attribute: hx-get
            The hx-get attribute will cause an element to issue a
            GET to the specified URL and swap the HTML into the DOM
            using a swap strategy

        :param value: URI to GET when the element is activated
        :return: An hx-get attribute to be added to your element
        '''

        return BaseAttribute("hx-get", value)

```

Where we can write

```python
button(
    [htmx.hx_get("/api/data")], 
    class_="btn primary"
)["Click me!"]
```
