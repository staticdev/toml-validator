"""Test cases for the console module."""
from unittest.mock import Mock

from click.testing import CliRunner
import pytest
from pytest_mock import MockFixture

from toml_validator import console


@pytest.fixture
def runner():
    return CliRunner()


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


def test_main_without_argument(runner: CliRunner):
    result = runner.invoke(console.main)
    assert result.exit_code == 2


def test_main_with_argument_success(
    runner: CliRunner,
    mock_validation_validate_extension: Mock,
    mock_validation_validate_toml_no_error: Mock,
):
    with runner.isolated_filesystem():
        with open("file.toml", "w") as f:
            f.write("content doesnt matter")

        result = runner.invoke(console.main, ["file.toml"])
        assert result.output == (
            "Reading file file.toml.\n" "No problems found parsing file file.toml!\n"
        )
        assert result.exit_code == 0


def test_main_with_argument_fail(
    runner: CliRunner,
    mock_validation_validate_extension: Mock,
    mock_validation_validate_toml_with_error: Mock,
):
    with runner.isolated_filesystem():
        with open("file.toml", "w") as f:
            f.write("content doesnt matter")

        result = runner.invoke(console.main, ["file.toml"])
        assert result.output == (
            "Reading file file.toml.\n" "Error(s) found: |some error description|.\n"
        )
        assert result.exit_code == 0


@pytest.mark.e2e
def test_main_without_arguments_in_production_env(runner: CliRunner):
    result = runner.invoke(console.main)
    assert result.exit_code == 2
