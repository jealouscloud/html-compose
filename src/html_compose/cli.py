import argparse
import fileinput

from . import translate_html


def from_html(args):
    is_stdin = args.html == "-"

    if is_stdin:
        print("Reading from stdin. Press Ctrl+D to finish.")

    try:
        html_content = "\n".join(
            [
                line
                for line in fileinput.input(files=args.html, encoding="utf-8")
            ]
        )
    except Exception as exc:
        print("Failed to read HTML content: {}".format(exc))
        return
    except KeyboardInterrupt:
        return

    if is_stdin:
        print("---\n")

    tresult = translate_html.translate(html_content, args.noimport)

    if tresult is None:
        print("Failed to translate HTML content")
        return

    if tresult.import_statement:
        print(tresult.import_statement, "\n")

    if tresult.custom_elements:
        print("\n".join(tresult.custom_elements))

    if len(tresult.elements) > 1:
        print(tresult.as_array())
    elif len(tresult.elements) == 1:
        print(tresult.elements[0])


def parse_html_translate(parser):
    parser.add_argument(
        "html",
        default="-",
        nargs="?",
        help="HTML file to translate (default: stdin)",
    )

    parser.add_argument(
        "-n",
        "--noimport",
        nargs="?",
        const="html_compose",
        default=None,
        help="Instead of importing each element, use the specified module name",
    )


def html_convert():
    parser = argparse.ArgumentParser(description="HTML to python translator")
    parse_html_translate(parser)
    args = parser.parse_args()
    from_html(args)


def cli():
    """
    Command-line tool to translate HTML to Python code using html_compose

    This function reads from stdin by default, but accepts an optional filename as argument
    """
    HTML_CONVERT = "convert"
    parser = argparse.ArgumentParser(description="html-compose cli")
    subparsers = parser.add_subparsers(dest="command")

    html_parser = subparsers.add_parser(
        HTML_CONVERT, help="Translate HTML to html-compose"
    )
    parse_html_translate(html_parser)
    args = parser.parse_args()
    if args.command == HTML_CONVERT:
        from_html(args)
    else:
        parser.print_help()
