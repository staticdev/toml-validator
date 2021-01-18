"""Test cases for the validation module."""
import pytest
from pytest_mock import MockFixture
from tomlkit.exceptions import TOMLKitError

from toml_validator.use_cases import toml


@pytest.fixture
def mock_tomlkit_parse(mocker: MockFixture) -> MockFixture:
    """Fixture for mocking tomlkit.parse."""
    return mocker.patch("tomlkit.parse")


@pytest.fixture
def mock_tomlkit_parse_exception(mocker: MockFixture) -> MockFixture:
    """Fixture for mocking tomlkit.parse."""
    mock = mocker.patch("tomlkit.parse")
    mock.side_effect = TOMLKitError("|some tomlkit error|")
    return mock


@pytest.fixture
def mock_open_valid_file(mocker: MockFixture) -> MockFixture:
    """Fixture for mocking build-in open for valid TOML file."""
    return mocker.patch("builtins.open", mocker.mock_open(read_data="[x]\na = 3"))


@pytest.fixture
def mock_open_invalid_file(mocker: MockFixture) -> MockFixture:
    """Fixture for mocking build-in open for valid TOML file."""
    return mocker.patch(
        "builtins.open", mocker.mock_open(read_data="[x]\na = 3\n[x]\na = 3")
    )


def test_validate_extension_valid() -> None:
    """It returns True when extension is valid."""
    assert toml.validate_extension("file.toml")


def test_validate_extension_invalid() -> None:
    """It returns False when extension is invalid."""
    assert not toml.validate_extension("file.xml")


def test_execute_no_error(
    mock_open_valid_file: MockFixture, mock_tomlkit_parse: MockFixture
) -> None:
    """It returns no errors when valid TOML."""
    assert toml.execute("file.toml") == ""


def test_execute_with_error(
    mock_open_invalid_file: MockFixture, mock_tomlkit_parse_exception: MockFixture
) -> None:
    """It returns errors when invalid TOML."""
    assert toml.execute("file.toml") == "|some tomlkit error|"


@pytest.mark.e2e
def test_execute_no_error_production(mock_open_valid_file: MockFixture) -> None:
    """It returns no errors when valid TOML (e2e)."""
    assert toml.execute("file.toml") == ""


@pytest.mark.e2e
def test_execute_with_error_production(mock_open_invalid_file: MockFixture) -> None:
    """It returns errors when invalid TOML (e2e)."""
    assert toml.execute("file.toml") == 'Key "x" already exists.'
