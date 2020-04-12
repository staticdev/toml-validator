"""Toml Validator CLI."""

import click

from . import __version__, validation


@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.version_option(version=__version__)
def main(filename: str) -> None:
    """Makes validations and echos errors if found."""
    validation.validate_extension(filename)

    click.secho("Reading file {}.".format(filename), fg="blue")

    errors = validation.validate_toml(filename)
    if errors:
        click.secho("Error(s) found: {}.".format(errors), fg="red")
    else:
        click.secho("No problems found parsing file {}!".format(filename), fg="green")
