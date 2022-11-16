#!/usr/bin/env python3

from .cmd import run


def get_diff(cached=False):
    """Get git revision diff

    Args:
        cached(bool): if True get diff in stage area. else, get diff from HEAD

    Returns:
        diff(str): git diff string
    """

    if cached:
        cmd = ["git", "diff", "--cached", "--", "'*.[chS]'"]
    else:
        cmd = ["git", "diff", "--", "'*.[chS]'"]

    return run(cmd, shell=True).stdout
