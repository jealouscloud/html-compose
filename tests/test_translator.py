import html_compose.translate_html as t


def test_translate():
    """
    Basic text of html -> html_compose translation
    """
    ht = """
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
              <input type="checkbox" role="switch" id="terms" name="terms" />
              I agree to the
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

    expected = section({"id": "preview"})[
        h2()["Preview"],
        pre()["  preformatted  "],
        pre()["          text\n\n        "],
        p()[
            "Sed ultricies dolor non ante vulputate hendrerit. Vivamus sit amet suscipit sapien. Nulla iaculis eros a elit pharetra egestas. "
        ],
        form()[
            input(
                {
                    "type": "text",
                    "name": "firstname",
                    "placeholder": "First name",
                    "aria-label": "First name",
                    "required": "",
                }
            ),
            input(
                {
                    "type": "email",
                    "name": "email",
                    "placeholder": "Email address",
                    "aria-label": "Email address",
                    "autocomplete": "email",
                    "required": "",
                }
            ),
            button({"type": "submit"})["Subscribe"],
            fieldset()[
                label({"for": "terms"})[
                    input(
                        {
                            "type": "checkbox",
                            "role": "switch",
                            "id": "terms",
                            "name": "terms",
                        }
                    ),
                    "I agree to the ",
                    a({"href": "#", "onclick": "event.preventDefault()"})[
                        "Privacy Policy"
                    ],
                ]
            ],
        ],
    ]
    lines = t.translate(ht).strip().splitlines()
    lines[1] = lines[1] + ".render()"
    output = eval("\n".join(lines[1:]))
    assert output == expected.render()
