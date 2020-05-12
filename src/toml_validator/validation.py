"""Toml Validator validations."""
import sys

import tomlkit
from tomlkit.exceptions import ParseError
from tomlkit.exceptions import TOMLKitError


def validate_extension(filename: str) -> bool:
    """Validates extension in filename.

    Args:
        filename (str): name of the file.

    Returns:
        bool: if extension is valid.
    """
    valid_extensions = [".toml"]
    for extension in valid_extensions:
        if filename.endswith(extension):
            return True
    sys.exit('Error: "FILANAME" {} does not have a valid extension.'.format(filename))


def validate_toml(filename: str) -> str:
    """It validates the TOML.

    Args:
        filename (str): name of the file.

    Returns:
        str: error messages.
    """
    with open(filename) as toml:
        lines = toml.read()

    try:
        tomlkit.parse(lines)
        return ""
    except (TOMLKitError, ParseError) as errors:
        return str(errors)
