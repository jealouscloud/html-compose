import argparse
import fileinput

from . import translate_html


def from_html(args):
    is_stdin = args.html == "-"

    if is_stdin:
        print("Reading from stdin. Press Ctrl+D to finish.")

    html_content = "\n".join(
        [line for line in fileinput.input(files=args.html, encoding="utf-8")]
    )
    if is_stdin:
        print("---\n")
    print(translate_html.translate(html_content))

def parse_html_translate(parser):
    parser.add_argument(
        "html",
        default="-",
        nargs="?",
        help="HTML file to translate (default: stdin)",
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
    HTML_CONVERT = "html-convert"
    parser = argparse.ArgumentParser(description="html-compose cli")
    subparsers = parser.add_subparsers(dest="command")

    html_parser = subparsers.add_parser(
        HTML_CONVERT, help="Translate HTML to html-compose"
    )
    parse_html_translate(html_parser)
    args = parser.parse_args()
    if args.command == HTML_CONVERT:
        from_html(args)
