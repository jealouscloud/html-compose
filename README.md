# html-compose

Composable HTML generation in python

## Features

-   Lazy evaluation
-   Natural syntax: Self attrs in `__init__`, children in `[brackets]` via `__getitem__`
-   Type hints for the editor generated from WhatWG spec

## Goals

-   Be a stable layer for further abstraction of client-server model applications and libraries
-   Put web developer documentation in the hands of developers via their IDE
-   Opinionate as few things as possible favoring expression, stay out of the way

## Magic decisions

The code base is littered with "**Magic**"" decisions to make your life easier, but the keen developer will want to know exactly what these are.

### Children

The children iterator/resolver makes some decisions to marshal input into strings

-   bools are translated to string `true`/`false`
-   floats passed as-is are converted to strings using a fixed precision. The default is defined in `ElementBase.FLOAT_PRECISION` and can be overridden in two ways
    -   Set `ElementBase.FLOAT_PRECISION` to the desired value - global
    -   Set `YourElement.FLOAT_PRECISION` to the desired value - applies just to the element
-   Callables: Children can be callables, like functions or classes that implement `__call__`.
## Inspiration

-   [Throw out your templates](https://github.com/tavisrudd/throw_out_your_templates) by Tavis Rudd
-   [The Principle](https://github.com/pydantic/FastUI?tab=readme-ov-file#the-principle-long-version) from pydantic FastUI
-   [htpy](https://github.com/pelme/htpy) for its syntax ideas, which itself is inspired by projects not in this list
-   [htmx](https://htmx.org/) As a way to transition to a "dumb client" model
-   [hyperaxe](https://github.com/ungoldman/hyperaxe) Similar tool for javascript
-   [flexx](https://github.com/flexxui/flexx) A python super toolkit for developing user applications
-   [lit](https://lit.dev/) lit and the web component engine that it wraps

# The WhatWG spec

The attributes are classes that live under `attributes`.

## Generating

In the virtual environment, run `python tools/spec_generator.py` followed by `python tools/generate_attributes.py`.

This will update the `tools/generated` directory

## Maintaining

They might be slightly different from the generated package as they're actively maintained.

Code generation was used as a trick to bootstrap this package quickly but future maintenance is important, as tools such as the popover API were recently added.

Maintainers will run the generating step, which will update the `tools/generated/` classes.

Updates pertaining to those changes should be shipped into the actual module under `src`

# Dependencies

-   PalletsProjects [markupsafe](https://github.com/pallets/markupsafe/) for text escaping
-   `beautifulsoup4` to optionally beautify HTML

# Development tools

-   Developed using [rye](https://rye.astral.sh/)
-   Linted and formatted with [ruff](https://docs.astral.sh/ruff/). [Differences from black](https://docs.astral.sh/ruff/formatter/black/)

# License

MIT.
