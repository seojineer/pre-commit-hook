#!/usr/bin/env python3

import sys

from .cmd import run


def get_diff(cached=False, files=None):
    """Get git revision diff

    Args:
        cached(bool): if True get diff in stage area. else, get diff from HEAD
        files(list): file list

    Returns:
        diff(str): git diff string
    """
    if files is None:
        sys.exit(0)

    if cached:
        cmd = ["git", "diff", "--cached", "--", " ".join(files)]
    else:
        cmd = ["git", "diff", "--", " ".join(files)]

    return run(cmd, shell=True).stdout
