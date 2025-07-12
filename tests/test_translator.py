from bs4 import BeautifulSoup

import html_compose.translate_html as t


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
        lines = "\n\n".join(tresult.elements) + ".render()"
        exec(tresult.import_statement)
        output = eval(lines)
        soup1 = BeautifulSoup(output, "html.parser")
        soup2 = BeautifulSoup(expected.render(), "html.parser")
        lines = str(soup1).splitlines()
        lines2 = str(soup2).splitlines()
        assert len(lines) == len(lines2)
        for i, line in enumerate(lines):
            assert line.strip() == lines2[i].strip(), (
                f"Line {i + 1} mismatch: {line.strip()} != {lines2[i].strip()}"
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
