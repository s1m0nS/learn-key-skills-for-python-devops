from mylib.calc import *
from calCLI import cli
from click.testing import CliRunner
import pytest


#
@pytest.fixture
def runner():
    return CliRunner()


# Write test functions for each function in calc.py


def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-3, -2) == -1


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(-6, 3) == -2
    with pytest.raises(ValueError):
        divide(5, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -1) == 0.5


# Write a test for each command in calCLI.py


def test_add_cmd(runner):
    result = runner.invoke(cli, ["add", "1", "2"])
    assert result.exit_code == 0
    assert "3.0" in result.output


def test_subtract_cmd(runner):
    result = runner.invoke(cli, ["subtract", "5", "3"])
    assert result.exit_code == 0
    assert "2.0" in result.output


def test_multiply_cmd(runner):
    result = runner.invoke(cli, ["multiply", "4", "2"])
    assert result.exit_code == 0
    assert "8.0" in result.output


def test_divide_cmd(runner):
    result = runner.invoke(cli, ["divide", "10", "2"])
    assert result.exit_code == 0
    assert "5.0" in result.output


def test_power_cmd(runner):
    result = runner.invoke(cli, ["power", "2", "3"])
    assert result.exit_code == 0
    assert "8.0" in result.output


def test_help(runner):
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "A calculator program" in result.output
