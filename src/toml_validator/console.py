""" Toml Validator CLI """

import glob
import sys
from typing import Optional

import click
from tomlkit import parse
from tomlkit.exceptions import TOMLKitError, ParseError

from . import __version__


def get_toml_filename() -> Optional[str]:
    """ Returns first csv filename in current folder """
    filenames = glob.glob("*.toml")
    if filenames:
        return filenames[0]
    return sys.exit(
        "Error: no file found, check the documentation for more info.")


@click.command()
@click.version_option(version=__version__)
def main() -> None:
    """ Gets TOML from current folder and validate  """
    filename = get_toml_filename()

    with open(filename) as toml:
        lines = toml.read()

    click.secho("Reading file %s" % filename, fg="blue")
    try:
        doc = parse(lines)
        click.secho("No problems found parsing file %s!" % filename, fg="green")
    except (TOMLKitError, ParseError) as error:
        click.secho("Error found: " + str(error), fg="red")


if __name__ == "__main__":
    main()
