# html-compose

✨ Composable HTML generation in Python 3.10+ with extensive type hinting 📚

```python
from html_compose import a, article, body, br, head, html, p, strong, title

>>> username = "github wanderer"
>>> print(
  html()[
    head()[title()[f"Welcome, {username}!"]],
    body()[
        article()[
            p()["Welcome to the internet", strong()[username], "!"],
            br(),
            p()[
                "Have you checked out this cool thing called a ",
                a(href="https://google.com")["search engine"],
                "?",
            ],
        ]
    ],
  ].render()
)
<html><head><title>Welcome, github wanderer!</title></head><body><article><p>Welcome to the internet<strong>github wanderer</strong>!</p><br /><p>Have you checked out this cool thing called a <a href="https://google.com">search engine</a>?</p></article></body></html>
```

## Features ✨

- ⚡ Lazy evaluation leading to performance gains
* 🛏 Define children via `[]` syntax:
  ```python
  from html_compose import p, strong
  p()["a", strong()["bold"], "statement"]
  #<p>a <strong>bold</strong> statement
  # The above is identical to
  p().append(["a", strong()["bold"], "statement"])
  ```
* 🧩 Skip constructor via same `[]` syntax for text only elements.
  ```python
  from html_compose import ul, li
  ul[
      li["Look ma!"]
      li["No constructor!"],
      li["This feels natural"],
      li["for text elements"]
  ]
  ```
* 🌐 Define attributes in a variety of ways:
  ```python
  from html_compose import div

  ## With type hints
  div(tabindex=1)
  div(attrs=[div.tabindex(1)])
  # <div tabindex=1></div>
  
  ## Positionally
  div([div.tabindex(1)])
  # <div tabindex=1></div>
  div({"data-for-something": "foo"})
  # <div data-for-something="foo"></div>
  ## With class dictionary resolution
  is_dark_mode = False
  div(class_={"dark-mode": is_dark_mode, "flex": True})
  # <div class="flex"></div>
  
  ## Combine the two `
  div(attrs=[div.class_("flex")], class_={"dark-mode": True})
  # <div class="flex dark-mode"></div>
  ```

- 🎭 Type hints for the editor generated from WhatWG spec

## Goals 🛠️

- Be a stable layer for further abstraction of client-server model applications and libraries
- Put web developer documentation in the hands of developers via their IDE
- 🚀 Opinionate as few things as possible favoring expression; stay out of the way
- Clearly mark any potentially breaking changes through discovered development optimizations in changelog

## Magic decisions 🪄

The code base is littered with "**Magic**" decisions to make your life easier, but the keen developer will want to know exactly what these are.

### Children 🌟

The children iterator/resolver makes some decisions to marshal input into strings:
- 🔒 All text elements and attribute values are escaped by default to prevent XSS
  - To inject unsafe text it must explicitly be marked unsafe via `html_compose.unsafe_text`.
- 💡 Bools are translated to string `true`/`false`
- ✨ Floats passed as-is are converted to strings by rounding to a fixed precision. The default is defined in `ElementBase.FLOAT_PRECISION` and can be overridden in two ways:
  - Set `ElementBase.FLOAT_PRECISION` to the desired value - global
  - Set `YourElement.FLOAT_PRECISION` to the desired value - applies just to the element. i.e. `td.FLOAT_PRECISION`
- 🏷️ Children can be callables, like functions, lambdas, or classes that implement `__call__`. These are resolved at render time.

## Inspiration ✨
Inspiration and motivation for this library are listed below.

- [Throw out your templates](https://github.com/tavisrudd/throw_out_your_templates) by Tavis Rudd
- [The Principle](https://github.com/pydantic/FastUI?tab=readme-ov-file#the-principle-long-version) from pydantic FastUI
- [htpy](https://github.com/pelme/htpy) for its syntax ideas, which itself is inspired by projects not in this list
- [htmx](https://htmx.org/) Transition library to a "dumb client" model
- [alpinejs](https://alpinejs.dev/) Another "dumb client" transition library
- [hyperaxe](https://github.com/ungoldman/hyperaxe) Similar tool for JavaScript
- [flexx](https://github.com/flexxui/flexx) A Python super toolkit for developing user applications
- [lit](https://lit.dev/) lit and the web component engine that it wraps

# The WhatWG spec 📝
The Web Hypertext Application Technology Working Group (WHATWG) is a community of people interested in evolving HTML and related technologies.

They produce a document which defines the HTML spec.

https://html.spec.whatwg.org

We parse this document to produce code-generated type hints and annotations.

## Generating ⚙️

For maintainers.

In the virtual environment, run `python tools/spec_generator.py` followed by `python tools/generate_attributes.py` or `python tools/generate_elements.py`

This will update the `tools/generated` directory.

We track this in git so we can see 1:1 changes to our generation.

The generated code is moved into the actual `src` directory and then the repo tooling is run over it:

- `rye lint --fix`
- `rye fmt`

## Maintaining ⚖️

Elements or attributes may be slightly different from the live package. These should be merged in.

Code generation was used as a trick to bootstrap this package quickly, but the web spec changes quickly, as tools such as the popover API were recently added.

Maintainers will run the generating step, which will update the `tools/generated/` classes.

Updates pertaining to those changes should be shipped into the actual module under `src`.

# Dependencies

- PalletsProjects [markupsafe](https://github.com/pallets/markupsafe/) for text escaping
- `beautifulsoup4` to optionally beautify HTML

# Development tools ⚙️

- Developed using [rye](https://rye.astral.sh/)
- Linted and formatted with [ruff](https://docs.astral.sh/ruff/). [Differences from black](https://docs.astral.sh/ruff/formatter/black/)

# License

MIT.

