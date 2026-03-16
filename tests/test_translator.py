from bs4 import BeautifulSoup

import html_compose.translate_html as t
from html_compose import render as render_nodes


def _render_translated(html: str) -> str:
    tresult = t.translate(html)
    env: dict[str, object] = {"__builtins__": __builtins__}
    if tresult.import_statement:
        exec(tresult.import_statement, env, env)
    if tresult.custom_elements:
        exec("\n".join(tresult.custom_elements), env, env)
    nodes = [eval(expr, env, env) for expr in tresult.elements]
    return render_nodes(nodes)


def test_translate():
    """
    Basic text of html -> html_compose translation
    """
    html = """
<section id="preview">
<h2>Preview</h2>
<pre>  preformatted  </pre>
<pre>
    text

</pre>
<p>
    Sed ultricies dolor non ante vulputate hendrerit. Vivamus sit amet suscipit sapien. Nulla
    iaculis eros a elit pharetra egestas.
</p>
<form>
    <input
    type="text"
    name="firstname"
    placeholder="First name"
    aria-label="First name"
    required
    />
    <input
    type="email"
    name="email"
    placeholder="Email address"
    aria-label="Email address"
    autocomplete="email"
    required
    />
    <button type="submit">Subscribe</button>
    <fieldset>
    <label for="terms">
        <input type="checkbox" role="switch" id="terms" name="terms" />I agree to the
        <a href="#" onclick="event.preventDefault()">Privacy Policy</a>
    </label>
    </fieldset>
</form>
</section>
      """
    from html_compose import (
        a,
        button,
        fieldset,
        form,
        h2,
        input,
        label,
        p,
        pre,
        section,
    )

    expected = section(id="preview")[
        h2()["Preview"],
        pre()["  preformatted  "],
        pre()["    text\n\n"],
        p()[
            "Sed ultricies dolor non ante vulputate hendrerit. Vivamus sit amet suscipit sapien. Nulla iaculis eros a elit pharetra egestas."
        ],
        form()[
            input(
                {"aria-label": "First name"},
                type="text",
                name="firstname",
                placeholder="First name",
                required="",
            ),
            " ",
            input(
                {"aria-label": "Email address"},
                type="email",
                name="email",
                placeholder="Email address",
                autocomplete="email",
                required="",
            ),
            " ",
            button(type="submit")["Subscribe"],
            fieldset()[
                label(for_="terms")[
                    input(
                        {"role": "switch"},
                        type="checkbox",
                        id="terms",
                        name="terms",
                    ),
                    "I agree to the ",
                    a({"onclick": "event.preventDefault()"}, href="#")[
                        "Privacy Policy"
                    ],
                ]
            ],
        ],
    ]

    tresult = t.translate(html)

    def _test_translation(r: t.TranslateResult):
        render_expr = "\n\n".join(tresult.elements) + ".render()"
        exec(tresult.import_statement)
        output = eval(render_expr)
        soup1 = BeautifulSoup(output, "html.parser")
        soup2 = BeautifulSoup(expected.render(), "html.parser")
        rendered_lines = str(soup1).splitlines()
        expected_lines = str(soup2).splitlines()
        assert len(rendered_lines) == len(expected_lines)
        for i, line in enumerate(rendered_lines):
            assert line.strip() == expected_lines[i].strip(), (
                f"Line {i + 1} mismatch: {line.strip()} != {expected_lines[i].strip()}"
            )

    _test_translation(t.translate(html))
    _test_translation(t.translate(html, "ht"))


def test_round_trip():
    html = (
        "<p>Another way to understand that text is to look at the word-for-word "
        "translation: <strong> in the home</strong> in the mind</p>"
    )

    stripped = (
        "<p>Another way to understand that text is to look at the word-for-word "
        "translation: <strong>in the home</strong> in the mind</p>"
    )
    tresult = t.translate(html)
    print(tresult.import_statement)
    exec(tresult.import_statement)
    if tresult.custom_elements:
        exec("\n".join(tresult.custom_elements))
    lines = "\n\n".join(tresult.elements) + ".render()"
    output = eval(lines)
    assert output == stripped


def test_script_round_trip():
    # Ensure that text nodes with <, >, & survive a round trip
    html = '<script>if (a < b && c > d) { console.log("hello & welcome"); }</script>'
    tresult = t.translate(html)
    print(tresult.import_statement)
    exec(tresult.import_statement)
    if tresult.custom_elements:
        exec("\n".join(tresult.custom_elements))
    lines = "\n\n".join(tresult.elements) + ".render()"
    print(lines)
    output = eval(lines)
    assert output == html


def test_inline_whitespace_between_phrasing_tags():
    html = "<p><span>foo</span> <span>bar</span></p>"
    assert _render_translated(html) == html


def test_inline_whitespace_trimmed_outside_phrasing():
    html = "<p> <div>block</div> </p>"
    expected = "<p><div>block</div></p>"
    assert _render_translated(html) == expected


def test_whitespace_only_between_phrasing_tags():
    html = "<p><span>foo</span>        <span>bar</span></p>"
    expected = "<p><span>foo</span> <span>bar</span></p>"
    assert _render_translated(html) == expected


def test_inline_whitespace_between_root_phrasing_tags():
    html = "<span>foo</span> <span>bar</span>"
    assert _render_translated(html) == html
