# Idea
The base element has tricks built into it so that you can write HTML faster.

## Implemented
(fill out something like this pls)
* `[]` syntax is a wrapper for `Element.append` i.e. `div().append`, except that it returns itself so that it can be chained: `div[ div["a", "b", "c"] ]`
* callable and iterator nesting `div()[callable, [ br(), "text" ]]`
* multi-parameter lambda function: div(data=[1,2,3])[lambda x: x.data]
    * 0 params: nothing
    * param 1: parent node, if applicable
    * param 2: its parent, if applicable

* `Element`.`attribute` i.e. `img.srcset()` with description, implemented as classes which are chldren of subclass.
* LRU cache
  * The basic attribute concat are called a lot and so they maintain an LRU cache configurable in size via `Element`.`ATTR_CACHE_SIZE` i.e. `div.ATTR_CACHE_SIZE`.
  * The multi-parameter lambda function also has an LRU cache to reduce time spent getting function params. This only works because it can guarantee it is only working on strings.
* The `class_` thing: You can't use `class` as an argument in Python. This alternative was chosen because it is identical to autocomplete.
* Each element has a `data` field which can be used in lambdas.

## Pending
* `with` nesting
```

with div(h1("Title")] as d:
  p("This is like a translated markdown document")
  br()
  p("So anyway, I started ")
  strong("blasting.")


```