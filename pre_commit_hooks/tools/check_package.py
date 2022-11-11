"""Check package exist"""

import importlib
from importlib.metadata import version as get_version
from shutil import which

from py_console import console


def check_py_package_version(name, version, verbose=False):
    """Check python package version

    Args:
        name(str): python package name
        version(str): python package version
        verbose(bool): show debug log if True.
    """

    try:
        installed_version = get_version(name)
        if verbose:
            console.info(f"[DEBUG] {name} version: {installed_version}", showTime=False)
        if installed_version != version:
            raise Exception(f"[ERROR] {name} version is not same as {version}.")
    except importlib.metadata.PackageNotFoundError:
        raise Exception(f"[ERROR] {name} not found.")


def check_package_exist(name, verbose=False):
    """Check if package installed

    Args:
        name(str): package name
        verbose(bool): show debug log if True.
    """

    if which(name) is None:
        raise Exception(f"[ERROR] {name} not found.")
    else:
        if verbose:
            console.info(f"[DEBUG] {name} exist.", showTime=False)
