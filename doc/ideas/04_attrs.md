# Idea
There are multiple ways to define attributes for an html element i.e.

```python
from html_compose import div
is_error = False

# keyword arg syntax (preferred)
# note that attrs that conflict with python keywords
# have an underscore_ appended. This was chosen so autocomplete still works.

div(class_="flex")
div(class_=["flex", "items-center"])
div(class_={
    "flex": True,
    "error": is_error == True
})
div(class_=div.hint.class_("flex"))

div(class_=div._.class_("flex"))
# div._ is a syntax shorthand for div.attrhint

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


```

## BaseAttribute
All attributes inherit BaseAttribute which defines a key and a value and resolves at render time.

The class attribute and style attribute have rules to split by their correct delimeter.

```python
from html_compose import div
is_red = False
# dict of dicts str:bool
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

## attrs= parameter syntax

In the constructor for any element you can specify the attrs paramter.

It can be either a list or a dictionary.

### Positional argument caveat
Although the documentation is explicit in using the `attrs` kwarg, `attrs` is
actually the first argument of the constructor and can be excluded i.e.
```python
div({"class": "flex"})
```

### list
```python
from html_compose.elements import a, div

div(attrs=[div.class_("red")])

a(attrs=[
    a.hint.href("https://google.com"),
    a.hint.tabindex(1),
    a.hint.class_(["flex", "flex-col"])
]
)

# string / list of string is explicitly NOT supported
# it requires disabling sanitization and is therefore quietly prone to XSS
div(attrs=['class="red"']) # ❌
```

### dict

```python
a(attrs={
    "href": a.hint.href("https://google.com")
    "tabindex': 1
})

div(attrs={
    "class": "red"
})



div(attrs={
    "class": ["flex", "items-center"]
})
```

## Keyword argument extension
An extention of the attr syntax was generated for all built-in HTML elements. It would be time-consuming to do this for custom element types, but code generation leans well into this case.

Traditionally, kwargs would be too non-descript to provide helpful editor hints.

To aid with fluent document writing, each element was generated with its attributes and a paired docstring
i.e.
`:param href: Address of the hyperlink`

```python
a(href="https://google.com", tabindex=1)
```

Under the hood, it's all translated to the BaseAttribute class and the value is
escaped before rendering.

# Breakdown

There's a number of options for declaring an attribute value defined below. These are to aid in very common operations such as building a `class` string.

## Attribute definitions
Care was put into generating attribute definitions for each class.

Anything found in the HTML specification document is available in an element's cousin attribute class.

i.e. the `img` class has a cousin class `ImgAttrs`.

We can access the definition of an attribute for that element via `ImgAttrs.$attr` i.e. `ImgAttrs.alt(value="demo")`. Each element, like `img`, has a child class which is an inheritor of its sibling attrs class  - `img.hint` inherits `ImgAttrs` so you can access the same definition via `img.hint.alt("...")`. 

Additionally, there's a `_` shorthand for `img.hint`. `img._` is just a reference to `img.hint`.

The purpose of this system is to provide full type hints.