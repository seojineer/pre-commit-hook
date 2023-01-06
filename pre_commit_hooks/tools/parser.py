"""Argument parser"""

import argparse


def get_parser(argv=None):
    """Default Parser

    Args:
        argv (list): string list to parse. default value is sys.argv.
    """

    parser = argparse.ArgumentParser(description="argument parser")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        help="show log as detail",
        action="store_true",
    )

    return parser
