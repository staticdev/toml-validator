"""Test cases for the __main__ module."""
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
def mock_validation_validate_extension(mocker: MockFixture) -> Mock:
    """Fixture for mocking validation.validate_extension."""
    return mocker.patch("toml_validator.validation.validate_extension")


@pytest.fixture
def mock_validation_validate_toml_no_error(mocker: MockFixture) -> Mock:
    """Fixture for mocking validation.validate_toml with no errors."""
    mock = mocker.patch("toml_validator.validation.validate_toml")
    mock.return_value = ""
    return mock


@pytest.fixture
def mock_validation_validate_toml_with_error(mocker: MockFixture) -> Mock:
    """Fixture for mocking validation.validate_toml with error."""
    mock = mocker.patch("toml_validator.validation.validate_toml")
    mock.return_value = "|some error description|"
    return mock


def test_main_without_argument(runner: click.testing.CliRunner) -> None:
    """It exits with a status code of 2."""
    result = runner.invoke(__main__.main)
    assert result.exit_code == 2


def test_main_with_argument_success(
    runner: click.testing.CliRunner,
    mock_validation_validate_extension: Mock,
    mock_validation_validate_toml_no_error: Mock,
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


def test_main_with_argument_fail(
    runner: click.testing.CliRunner,
    mock_validation_validate_extension: Mock,
    mock_validation_validate_toml_with_error: Mock,
) -> None:
    """It outputs error."""
    with runner.isolated_filesystem():
        with open("file.toml", "w") as f:
            f.write("content doesnt matter")

        result = runner.invoke(__main__.main, ["file.toml"])
        assert result.output == (
            "Reading file file.toml.\n" "Error(s) found: |some error description|.\n"
        )
        assert result.exit_code == 0


@pytest.mark.e2e
def test_main_without_arguments_in_production_env(
    runner: click.testing.CliRunner,
) -> None:
    """It exits with a status code of 2 (e2e)."""
    result = runner.invoke(__main__.main)
    assert result.exit_code == 2
