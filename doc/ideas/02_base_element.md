# Idea

The base element has tricks built into it so that you can write HTML faster.

## Concepts

### [] syntax for children

`[]` syntax is a wrapper for `Element.append` i.e. `div().append`, except that it returns itself so that it can be chained: `div[ div["a", "b", "c"] ]`

Under the hood, this is just `BaseElement.__getitem__`

### [] syntax constructor

Normally you would construct an element like `h1()["My header"]`.

You can also do `h1["My header"]`.

You will notice this bypasses running the constructor.

Under the hood, this is just `BaseElement.__class_getitem__` which just runs the constructor with no parameters.
This shorthand can save a few keystrokes.

### Iterators / callables

You can nest iterators and even place callables in your children. i.e. `div()[lambda: "evaluated at render time", [ br(), "text" ]]`

### Lambda parameters

multi-parameter lambda function: `div()[lambda node, parent_if_avail: "Demo"]`
_ 0 params: nothing
_ param 1: parent node, if applicable \* param 2: its parent, if applicable

Element attributes aren't currently intended to be accessed to prevent mistreating HTML as data or application state, so these parameters would most likely be more useful in a custom extension of an element.

### Attribute classes

You can access `Element`.`attribute` i.e. `img.srcset()` with description, implemented as classes which are chldren of subclass.
These can be passed in element initialization `a(attrs=[a.href("https://google.com")])` and has the benefit of auto-complete.

### LRU cache

- The basic attribute concat are called a lot and so they maintain an LRU cache configurable in size via `Element`.`ATTR_CACHE_SIZE` i.e. `div.ATTR_CACHE_SIZE`. This only works because it can guarantee it is only working on strings.
- The multi-parameter lambda function also has an LRU cache to reduce time spent getting function params.

### Name conflicts

Examples:

- `class_`
- `del_`

You can't use `class` as an argument in Python because it is a keyword. We opt to call it `class_`

This alternative was chosen because it is identical to autocomplete.

The same rule is applied anywhere else a name conflicts with a keyword i.e. the `del` element.

### Repeat attributes

In the event `class` or `style` occur multiple times, they are concatenated with the correct delimeter in the order they're received.

Because there's no clear way to concat other attributes, an exception is raised.

### XSS prevention / automatic escape

Unescaped child nodes i.e. strings are automatically escaped to prevent XSS.

This is done by the palletsprojects `markupsafe` library.
