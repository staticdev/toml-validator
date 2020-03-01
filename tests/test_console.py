import click.testing
import pytest

from toml_validator import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


# TODO make the two success cases
# (one using mock file and one running a valid file in e2e)


def test_main_without_arguments(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 2


@pytest.mark.e2e
def test_main_without_arguments_in_production_env(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 2
