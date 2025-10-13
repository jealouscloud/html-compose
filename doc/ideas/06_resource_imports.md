# Resource imports (js / css / fonts)

There are now many standards in the web platform for correctly importing
your remote resources.

We no longer need to use nodejs and bundling to use module import semantics.

We can preload js and assign it a module name for importing.

We give helpers for managing css/js imports and the many attributes needed
to successfully preload and validate resource integrity.

We also give two font helpers, one for fonts resolved in css and one for
manually setting up .woff/etc font imports.

## Browser tech overview

- https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules
- https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/modulepreload
- https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload

## How our library makes resource setup better

By providing small helpers, we reduce the amount of redundant html to write.

```python
import html_compose.elements as el
from html_compose.resource import css_import, js_import, to_elements
from html_compose.document import document_generator

def get_css():
    return [
        css_import("./static/admin.css", cache_bust=False),
        css_import(
            "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css",
            hash=(
                "sha384-9ndCyUaIbzAi2FUVXJi0CjmCapS"
                "mO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM"
            ),
            crossorigin="anonymous",
            preload=True,
        ),
    ]

def get_js():
    return [
        js_import("./static/admin.js", name="admin", cache_bust=True),
        js_import(
            "https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm",
            name="alpinejs",
            preload=True,
            hash=(
                "sha384-Yf57wlxlrA1+0X6Ye9NOBxQ1tpmiwI/"
                "9mFpv9tT/Rh2UAajwwAlTWHnvTGYhgv7p"
            ),
            crossorigin="anonymous",
        ),
    ]


def get_fonts():
    return [
        font_import_manual(
            "./static/fonts/MyFont.woff2",
            family="MyFont",
            weight="normal",
            style="normal",
            display="swap",
            cache_bust=False,
        ),
        font_import_provider(
            href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap",
            preconnect=[
                "https://fonts.googleapis.com",
                "https://fonts.gstatic.com",
            ],
            preconnect_crossorigin="anonymous",
        ),
    ]



def test_importer():
    css = get_css()
    js = get_js()
    elements = to_elements(js, css)
    print(el.head()[elements].render())


def test_document_generator():
    css = get_css()
    js = get_js()
    print(document_generator(
        title="demo",
        lang="en",
        js=js,
        css=css,
        body_content=[el.h1("Hello world")])

```

**test_importer:**

```html
<head>
  <link
    href="https://fonts.googleapis.com"
    crossorigin="anonymous"
    rel="preconnect"
  />
  <link
    href="https://fonts.gstatic.com"
    crossorigin="anonymous"
    rel="preconnect"
  />
  <link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
    integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM"
    crossorigin="anonymous"
    as="style"
    rel="preload"
  />
  <link
    href="https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm"
    integrity="sha384-Yf57wlxlrA1+0X6Ye9NOBxQ1tpmiwI/9mFpv9tT/Rh2UAajwwAlTWHnvTGYhgv7p"
    crossorigin="anonymous"
    rel="modulepreload"
  />
  <link
    href="./static/fonts/MyFont.woff2"
    type="font/woff2"
    as="font"
    rel="preload"
  />
  <link href="./static/admin.css" rel="stylesheet" />
  <link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
    integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM"
    crossorigin="anonymous"
    rel="stylesheet"
  />
  <link
    href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&amp;display=swap"
    rel="stylesheet"
  />
  <style>
    @font-face {
      font-family: "MyFont";
      src: url("./static/fonts/MyFont.woff2");
      font-style: normal;
      font-display: swap;
      font-weight: normal;
    }
  </style>
  <script type="importmap">
    {
      "imports": {
        "admin": "./static/admin.js?ts=1760157623",
        "alpinejs": "https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm"
      }
    }
  </script>
  <script src="./static/admin.js?ts=1760157623" type="module"></script>
  <script
    src="https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm"
    type="module"
    integrity="sha384-Yf57wlxlrA1+0X6Ye9NOBxQ1tpmiwI/9mFpv9tT/Rh2UAajwwAlTWHnvTGYhgv7p"
    crossorigin="anonymous"
  ></script>
</head>
```

**test_document**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <title>demo</title>
    <link
      href="https://fonts.googleapis.com"
      crossorigin="anonymous"
      rel="preconnect"
    />
    <link
      href="https://fonts.gstatic.com"
      crossorigin="anonymous"
      rel="preconnect"
    />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
      integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM"
      crossorigin="anonymous"
      as="style"
      rel="preload"
    />
    <link
      href="https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm"
      integrity="sha384-Yf57wlxlrA1+0X6Ye9NOBxQ1tpmiwI/9mFpv9tT/Rh2UAajwwAlTWHnvTGYhgv7p"
      crossorigin="anonymous"
      rel="modulepreload"
    />
    <link
      href="./static/fonts/MyFont.woff2"
      type="font/woff2"
      as="font"
      rel="preload"
    />
    <link href="./static/admin.css" rel="stylesheet" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
      integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM"
      crossorigin="anonymous"
      rel="stylesheet"
    />
    <link
      href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&amp;display=swap"
      rel="stylesheet"
    />
    <style>
      @font-face {
        font-family: "MyFont";
        src: url("./static/fonts/MyFont.woff2");
        font-style: normal;
        font-display: swap;
        font-weight: normal;
      }
    </style>
    <script type="importmap">
      {
        "imports": {
          "admin": "./static/admin.js?ts=1760157623",
          "alpinejs": "https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm"
        }
      }
    </script>
    <script src="./static/admin.js?ts=1760157623" type="module"></script>
    <script
      src="https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm"
      type="module"
      integrity="sha384-Yf57wlxlrA1+0X6Ye9NOBxQ1tpmiwI/9mFpv9tT/Rh2UAajwwAlTWHnvTGYhgv7p"
      crossorigin="anonymous"
    ></script>
  </head>

  <body>
    <h1>Hello world</h1>
  </body>
</html>
```

## Where to go from here

We've informed the browser how to optimally and in parallel load our resources.

Now we are free to develop without bundling javascript if we so desire.

Heck, you could even map a package.json used in your development environment
into a `js_import` generator.

The sky is the limit.
