"""Argument parser"""

import argparse


def get_args(argv=None):
    """Parse argument

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

    return parser.parse_args(argv)
