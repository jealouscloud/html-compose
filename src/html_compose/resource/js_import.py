from typing import Iterable, Literal

from .. import elements as el
from ..util_funcs import flatten_iterable, is_iterable_but_not_str
from .util_funcs import _cachebust_resource_uri


class js_import:
    """
    A javascript import helper class which employs one or more of:

    - `script(` to define the import
    - `importmap` which maps javascript module names to URLs
    Setting the name parameter like so
    ```python
    js_import(
        "https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm",
        name="alpinejs")
    ```
    creates an import map so javascript modules can be imported by name
    - `link(rel="modulepreload")` to preload the import
    - if cache_bust is true, appends a timestamp to the URL to

    An production usage might look like:

    ```python
    [
    js_import('./static/admin.js',
                name='admin',
                cache_bust=True),

    js_import(
        "https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm",
        name="alpinejs",
        preload=True,
        hash=(
            "sha384-Yf57wlxlrA1+0X6Ye9NOBxQ1tpmiwI/"
            "9mFpv9tT/Rh2UAajwwAlTWHnvTGYhgv7p"
            ),
        crossorigin="anonymous"
        ),

    ]
    ```

    ...

    ## Usage in window:

    ```python
    script(type="module")[
        '''
        import Alpine from 'alpinejs'
        window.Alpine = Alpine
        Alpine.start()
        '''
    ]
    ```

    ## Generated "HTML":

    ```python
    import json
    from html_compose import el, unsafe_text

    [
        el.script(type="importmap")[
            unsafe_text('{"imports": {"admin": "./static/admin.js?ts=1760157623", "alpinejs": "https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm"}}')
        ],

        el.link(href="./static/admin.js?ts=1760157623", rel=["modulepreload"]),


        el.link(
            href="https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm",
            integrity="sha384-Yf57wlxlrA1+0X6Ye9NOBxQ1tpmiwI/9mFpv9tT/Rh2UAajwwAlTWHnvTGYhgv7p",
            crossorigin="anonymous",
            rel=["modulepreload"],
        ),

        el.script(src="./static/admin.js?ts=1760157623", type="module"),

        el.script(
            src="https://cdn.jsdelivr.net/npm/alpinejs@3.15.0/+esm",
            type="module",
            integrity="sha384-Yf57wlxlrA1+0X6Ye9NOBxQ1tpmiwI/9mFpv9tT/Rh2UAajwwAlTWHnvTGYhgv7p",
            crossorigin="anonymous",
        ),
    ]
    ```

    See:
    - https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type/importmap
    - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules
    - https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/modulepreload
    - https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload
    - https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity
    - https://www.srihash.org/

    """

    def __init__(
        self,
        source: str,
        name: str | None = None,
        preload: bool = False,
        hash: str | None = None,
        async_: bool = False,
        defer: bool = False,
        nomodule: bool = False,
        scope_url: str | Iterable[str] | None = None,
        crossorigin: Literal["", "anonymous", "user-credentials"]
        | str
        | None = None,
        cache_bust: bool = False,
    ):
        """
        A javascript import wrapper to manage optimal window import strategies.

        If name is set, the import is added to an import map and imported
        as a module.

        Parameters
        ----------
        `source`:
            The literal src passed to tags i.e. script and link preload.

            If cache_bust is set, a timestamp is appended to the URL.
        `name`:
            The name of the import, e.g. "lodash" which can be used in
            javascript type="module" imports.

            Doing this automatically changes the script type to module

        `preload`:
            The modulepreload keyword, for the rel attribute of the `<link/>`
            element, provides a declarative way to preemptively fetch a module
            script, parse and compile it, and store it in the document's module
            map for later execution.

            If this is not a javascript module (i.e. name is not set),
            the rel attribute is set to "preload" and the as_ attribute
            is set to "script" instead.

        `async_`:
            The async attribute causes the script to be executed asynchronously as soon as it is available,
            without blocking HTML parsing.

        `defer`:
            Defers script execution until document parsing is complete.
            Has no effect on module scripts (they are deferred by default).

        `nomodule`:
            Added to script tag.

            Indicates that the script should not be executed in browsers that
            support ES modules — in effect, this can be used to serve fallback
            scripts to older browsers that do not support javascript modules.

        `hash`:
            An optional SRI integrity hash for the import

        `crossorigin`:
            Optionally sets the crossorigin attribute on the script tag.
            Valid values are "", "anonymous", "use-credentials"

        `cache_bust`:
            If true, appends a timestamp to the URL to work with browser
            caching. Webservers configured for static resources manage this
            feature automatically, but for development this can be useful.

            This feature only works for local resources, i.e. those that
            exist relative to `resource.settings.base_dir`

        `scope_url`:
            Optional route or list of paths where this import should be
            included.

            Scopes let you have different mappings for different parts of your
            app.

            Because they affect the import map but not what is loaded -
            the script tag controls what loads - they are rarely used.

        """

        self.name = name
        self.source = source
        self.preload = preload
        self.hash = hash
        self.scope_url = scope_url
        if scope_url and is_iterable_but_not_str(scope_url):
            self.scope_url = flatten_iterable(scope_url)
        self.crossorigin = crossorigin
        self.cache_bust = cache_bust
        self.has_link = preload
        self.async_ = async_
        self.defer = defer
        self.nomodule = nomodule
        self._src = self.uri()
        if hash and self.crossorigin is None:
            raise ValueError(
                "If hash is set, crossorigin must be set to ''/'anonymous'"
            )

    def uri(self) -> str:
        """
        Returns the source URI - with cache busting if enabled
        which is implemented by getting the mtime of the local file

        This operation performs up to two fs stats per call

        1. The base static directory is checked once and cached per interpreter
        2. The specific resource is checked if it is time to poll again
           based on settings.stat_poll_interval
        """
        if not self.cache_bust:
            return self.source

        return _cachebust_resource_uri(self.source)

    def import_map_entry(
        self,
    ) -> tuple[str, str] | tuple[str, str, Iterable] | None:
        """
        Returns a tuple of (name, source, scope_url) for use in an import map
        """
        if self.name:
            if self.scope_url is None:
                return (self.name, self._src)
            else:
                return (self.name, self._src, self.scope_url)

        return None

    def preload_link(self) -> el.link | None:
        """
        Returns one or more link element for this import
        """
        if self.preload:
            attrs = {"href": self._src}
            if self.hash:
                attrs["integrity"] = self.hash
            if self.crossorigin:
                attrs["crossorigin"] = self.crossorigin
            if self.name:
                return el.link(attrs=attrs, rel="modulepreload")
            else:
                return el.link(attrs=attrs, rel="preload", as_="script")

        return None

    def script(self) -> el.script:
        """
        Returns a script tag for this import
        """
        attrs: dict[str, str | bool] = {"src": self._src}

        if self.name:
            attrs["type"] = "module"
        if self.hash:
            attrs["integrity"] = self.hash
        if self.crossorigin:
            attrs["crossorigin"] = self.crossorigin
        if self.async_:
            attrs["async"] = True
        if self.defer and not self.name:
            # Only set defer for non-modules
            attrs["defer"] = True
        if self.nomodule:
            attrs["nomodule"] = True

        return el.script(attrs=attrs)
