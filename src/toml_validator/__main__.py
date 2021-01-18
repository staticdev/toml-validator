"""Command-line interface."""
import pathlib
import sys
from typing import Iterable
from typing import Iterator
from typing import Set
from typing import Tuple

import click

import toml_validator.use_cases.toml as toml


def _get_recursive_supported_files(
    paths: Iterable[pathlib.Path],
) -> Iterator[pathlib.Path]:
    """Recursively return the path to supported files."""
    for path in paths:
        if path.is_dir():
            yield from _get_recursive_supported_files(path.iterdir())
        elif path.is_file() and toml.validate_extension(str(path)):
            yield path


def get_files(src: Tuple[str, ...]) -> Set[pathlib.Path]:
    """Return all paths from list of arguments."""
    files = set()
    for i in src:
        p = pathlib.Path(i)
        if p.is_file():
            files.add(p)
        else:
            files.update(_get_recursive_supported_files(p.iterdir()))
    return files


@click.command()
@click.argument(
    "src",
    nargs=-1,
    type=click.Path(exists=True, file_okay=True, dir_okay=True, readable=True),
)
@click.version_option()
def main(src: Tuple[str, ...]) -> None:
    """Makes validations and echos errors if found.

    Args:
        src: name of validated file.

    Return status:
    * 0: no errors found
    * 1: incorrect usage
    * 2: invalid path
    * 3: errors found
    """
    files = get_files(src)

    if not files:
        click.secho("No file to check.")
        sys.exit(0)

    errors_found = False
    for file in files:
        click.secho(f"Reading file {file}.", fg="blue")

        errors = toml.execute(str(file))
        if errors:
            click.secho(f"Error(s) found on file {file}: {errors}.", fg="red")
            errors_found = True
        else:
            click.secho(f"No problems found parsing file {file}!", fg="green")

    if errors_found:
        sys.exit(3)


if __name__ == "__main__":
    main()  # pragma: no cover
