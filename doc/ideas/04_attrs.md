# Idea
There are multiple ways to design attribute setting for an html element i.e.

```python
is_red = False
# dict of dicts str:bool
# truthy = rendered
# falsey = ignored
div(attrs={
    "class": {
        'red': is_red,
        'blue': not is_red
    }
})

# dict of lists (the lists are joined with whitespace)
div[attrs={
    "class": ["red", "center"]
}]

# dict of strs
div(attrs={
    "class": "red"
})

# list of BaseAttribute
div(attrs=[div.class_("red")])

# string / list of string is explicitly NOT supported
# it is prone to XSS because it is not sanitized
div(attrs=['class="red"']) # ❌

```