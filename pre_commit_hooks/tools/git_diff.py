#!/usr/bin/env python3

from .cmd import run


def get_diff(prev_rev=None, cached=False):
    """Get git revision diff

    Args:
        prev_rev(str): previous git commit hash
        cached(bool): if True get diff in stage area. else, get diff from prev_rev to HEAD

    Returns:
        diff(str): git revision diff string
    """

    if cached:
        cmd = ["git", "diff", "--cached", "--", "'*.[chS]'"]
    else:
        cmd = ["git", "diff", prev_rev, "--", "'*.[chS]'"]

    return run(cmd, shell=True).stdout
