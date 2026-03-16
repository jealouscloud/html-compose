import argparse
import fileinput
import sys

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

    tresult = translate_html.translate(
        html_content, args.noimport, args.constructor
    )

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

    parser.add_argument(
        "-c",
        "--constructor",
        action="store_true",
        help="Always output element constructor",
    )


def html_convert():
    parser = argparse.ArgumentParser(description="HTML to python translator")
    parse_html_translate(parser)
    args = parser.parse_args()
    from_html(args)


def parse_gallery(parser):
    parser.add_argument("module", help="Path to the module to run")
    parser.add_argument(
        "--host",
        default="localhost",
        help="Host to run the gallery server on (default: localhost)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to run the gallery server on (default: 8000)",
    )
    parser.add_argument(
        "--livereload-host",
        default="(host)",
        help="Host to run the gallery server on (defaults to host value)",
    )
    parser.add_argument(
        "--livereload-port",
        type=int,
        default=51353,
        help="Port to run the gallery server on (default: 51353)",
    )
    parser.add_argument(
        "--force-polling",
        action="store_true",
        help="Force polling for file changes instead of using inotify or similar",
    )
    parser.add_argument(
        "--watch-extra-path",
        action="append",
        default=[],
        help="Additional paths to watch for changes (can be specified multiple times)",
    )
    parser.add_argument(
        "--python-path",
        nargs="?",
        help="Add path to Python search path",
        default=".",
    )


def gallery(args):
    from .gallery.server import run

    if args.python_path:
        if args.python_path not in sys.path:
            sys.path.insert(0, args.python_path)

    try:
        run(
            module_path=args.module,
            host=args.host,
            port=args.port,
            force_polling=args.force_polling,
            extra_paths=args.watch_extra_path,
            livereload_host=args.livereload_host
            if args.livereload_host != "(host)"
            else args.host,
            livereload_port=args.livereload_port,
        )
    except KeyboardInterrupt:
        print("\nExiting...")


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
    gallery_parser = subparsers.add_parser(
        "gallery", help="Run an HTML gallery server"
    )
    parse_gallery(gallery_parser)
    args = parser.parse_args()
    if args.command == HTML_CONVERT:
        from_html(args)
    elif args.command == "gallery":
        gallery(args)
    else:
        parser.print_help()
