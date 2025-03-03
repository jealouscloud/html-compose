# String Iterators and Tree Resolution in HTML Generation

## Core Concepts

1. Generators are beneficial to performance

- Elements are generated one at a time and immediately consumed by the join operation. You never store the complete set in memory.
- Each element is processed exactly once as it flows through the generator pipeline.
- Lazy evaluation: The HTML is generated on-demand, which is particularly valuable when building conditional elements or working with large datasets.
-

2. String Iterators:

- Used as the output of the `__html__` method, which represents sanitized elements and markup which is implemented as `deferred_resolve` in our base element class,

3. Tree Resolution: The process of walking through the HTML element tree and resolving all children.

## Concept: Iterator flattening

An iterator can contain iterators, like this:

```python
ul[ (li["one"], li["two"]) ]
```

This allows syntax like this:

```python
def get_items(db):
        return (
            li[
                h[row.name],
                h2[row.type]
                p[row.value]
            ] for row in db.query.stuff("select name, type, value ...")
    )
ul[ get_items(db_session) ]
```

## Concept: Tree Resolution

To resolve element.children into a list of strings, we first have to recursively walk the html element tree and yield all resolved children

We want to resolve the following in two ways.

```python
def get_article_content(_id):
    return "my article content"

article[
    h1["My cool article"],
    p(id="article-1")[
        lambda p: database.get_article_content(p.id)
    ]
]
```

### Deferred resolve

The **deferred resolve** step will resolve an iterator that looks a lot like this, as a list:

```python
[
    "<article>",

    "<h1>", "My cool article", "</h1>",

    "<p id='article-1'>",
    lambda: database.get_article_content()
    "</p>",

    "</article>"
]
```

As you can see, the static content that resolves is returned, but callables are returned as themselves.

### Full resolution

We simply walk the iterator generated in the deferred resolve step and call any callables before returning to `str.join`.

We believe a few cool things can be done with this regarding content generation and rendering.

The snippet above turns into

```python

"<p>",
  "my article content"
"</p>",
```

### Basic HTML iterator

The `deferred_resolve` method in our `BaseElement` class is a generator that yields HTML strings is similar to the following:

```python
def deferred_resolve(self):
    attrs = self.resolve_attrs()
    children = None if self.is_void_element else [child for child in self.resolve_tree()]

    # Yield opening tag, children, and closing tag
    yield f"<{self.name} {attr_string}>"
    if children:
        yield from children
    yield f"</{self.name}>"
```
