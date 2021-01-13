"""Command-line interface."""
import sys

import click

from . import validation


@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.version_option()
def main(filename: str) -> None:
    """Makes validations and echos errors if found.

    Args:
        filename: name of validated file.

    Return status:
    * 0: no errors found
    * 1: incorrect usage
    * 2: invalid path
    * 3: errors found
    """
    validation.validate_extension(filename)

    click.secho("Reading file {}.".format(filename), fg="blue")

    errors = validation.validate_toml(filename)
    if errors:
        click.secho("Error(s) found: {}.".format(errors), fg="red")
        sys.exit(3)
    else:
        click.secho("No problems found parsing file {}!".format(filename), fg="green")


if __name__ == "__main__":
    main()  # pragma: no cover
