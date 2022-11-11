#!/usr/env/python3


def get_retry_msg(diff_command, test_command):
    """Get retry message

    Args:
        diff_command(str): command to get diff
        lint_command(str): command that run lint
    """

    return (
        "Please execute '" + diff_command + " | " + test_command + "' on top directory."
    )
