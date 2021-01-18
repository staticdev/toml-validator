"""Test cases for the __main__ module."""
import os
import pathlib
from typing import Any
from unittest.mock import Mock

import click.testing
import pytest
from pytest_mock import MockFixture

from toml_validator import __main__


@pytest.fixture
def runner() -> click.testing.CliRunner:
    """Fixture for invoking command-line interfaces."""
    return click.testing.CliRunner()


@pytest.fixture
def mock_use_case_toml_validate_extension(mocker: MockFixture) -> Any:
    """Fixture for mocking toml.validate_extension."""
    return mocker.patch("toml_validator.use_cases.toml.validate_extension")


@pytest.fixture
def mock_use_case_toml_no_error(mocker: MockFixture) -> Any:
    """Fixture for mocking toml.execute with no errors."""
    mock = mocker.patch("toml_validator.use_cases.toml.execute")
    mock.return_value = ""
    return mock


@pytest.fixture
def mock_use_case_toml_with_error(mocker: MockFixture) -> Any:
    """Fixture for mocking toml.execute with error."""
    mock = mocker.patch("toml_validator.use_cases.toml.execute")
    mock.return_value = "|some error description|"
    return mock


def test_get_files_file(runner: click.testing.CliRunner) -> None:
    """It returns same file."""
    with runner.isolated_filesystem():
        with open("file.toml", "w") as f:
            f.write("content doesnt matter")

        src = "file.toml"
        expected = [pathlib.Path("file.toml")]
        sources = list(__main__.get_files((src,)))
        assert sorted(expected) == sorted(sources)


def test_get_files_directory(runner: click.testing.CliRunner) -> None:
    """It returns file in directory."""
    with runner.isolated_filesystem():
        os.mkdir("dir")
        with open("dir/file.toml", "w") as f:
            f.write("content doesnt matter")

        src = "dir"
        expected = [pathlib.Path("dir/file.toml")]
        sources = list(__main__.get_files((src,)))
        assert sorted(expected) == sorted(sources)


def test_get_files_nested_directory(runner: click.testing.CliRunner) -> None:
    """It returns file in subdirectory."""
    with runner.isolated_filesystem():
        os.mkdir("dir")
        os.mkdir("dir/dir2")
        with open("dir/file.notoml", "w") as f:
            f.write("content doesnt matter")
        with open("dir/dir2/file.toml", "w") as f:
            f.write("content doesnt matter")

        src = "dir"
        expected = [pathlib.Path("dir/dir2/file.toml")]
        sources = list(__main__.get_files((src,)))
        assert sorted(expected) == sorted(sources)


def test_main_without_argument(runner: click.testing.CliRunner) -> None:
    """It exits with a status code of 0."""
    result = runner.invoke(__main__.main)
    assert result.output == "No file to check.\n"
    assert result.exit_code == 0


def test_main_with_argument_success(
    runner: click.testing.CliRunner,
    mock_use_case_toml_validate_extension: Mock,
    mock_use_case_toml_no_error: Mock,
) -> None:
    """It exits with a status code of zero."""
    with runner.isolated_filesystem():
        with open("file.toml", "w") as f:
            f.write("content doesnt matter")

        result = runner.invoke(__main__.main, ["file.toml"])
        assert result.output == (
            "Reading file file.toml.\n" "No problems found parsing file file.toml!\n"
        )
        assert result.exit_code == 0


def test_main_with_invalid_path(
    runner: click.testing.CliRunner,
    mock_use_case_toml_validate_extension: Mock,
    mock_use_case_toml_with_error: Mock,
) -> None:
    """It outputs error."""
    with runner.isolated_filesystem():
        with open("file.toml", "w") as f:
            f.write("content doesnt matter")

        result = runner.invoke(__main__.main, ["file.to"])
        assert result.output.startswith("Usage:")
        assert result.exit_code == 2


def test_main_with_errors(
    runner: click.testing.CliRunner,
    mock_use_case_toml_validate_extension: Mock,
    mock_use_case_toml_with_error: Mock,
) -> None:
    """It outputs error."""
    with runner.isolated_filesystem():
        with open("file.toml", "w") as f:
            f.write("content doesnt matter")

        result = runner.invoke(__main__.main, ["file.toml"])
        assert result.output == (
            "Reading file file.toml.\n"
            "Error(s) found on file file.toml: |some error description|.\n"
        )
        assert result.exit_code == 3
