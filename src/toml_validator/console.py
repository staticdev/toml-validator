""" Toml Validator CLI """

import sys

import click
from tomlkit import parse
from tomlkit.exceptions import TOMLKitError, ParseError

from . import __version__


@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.version_option(version=__version__)
def main(filename) -> None:
    """ Gets TOML file and validate  """
    if not filename.endswith(".toml"):
       sys.exit("Error: \"FILANAME\" %s does not have a \".toml\" extension." % filename)

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
