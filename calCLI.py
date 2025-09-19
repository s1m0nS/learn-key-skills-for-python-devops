#!usr/bin/python

from mylib.calc import add, subtract, multiply, divide, power
import click


@click.group()
def cli():
    """A calculator program"""

@cli.command("add")
@click.argument("a", type=float)
@click.argument("b", type=float)

def add_cmd(a, b):
    """ "
    Add two numbers

    Example:
    ./calCLI.py add 5 10
    """

    # use colored output to print the results
    click.secho(f"{a} + {b} = {add(a, b)}", fg="green")

# -----------------------------------------------------------

def subtract_cmd(a, b):
    """
    Subtract two numbers

    Example:
    ./calCLI.py subtract 10 5
    """
    click.secho(f"{a} - {b} = {subtract(a, b)}", fg="green")

# -----------------------------------------------------------

def multiply_cmd(a, b):
    """
    Multiply two numbers

    Example:
    ./calCLI.py multiply 5 10
    """
    click.secho(f"{a} - {b} = {multiply(a, b)}", fg="green")

# -----------------------------------------------------------

def divide_cmd(a, b):
    """
    Divide two numbers

    Example:
    ./calCLI.py divide 10 2
    """
    if b == 0:
        click.secho("Error: Cannot divide by zero", fg="red")
    else:
        click.secho(f"{a} / {b} = {divide(a, b)}", fg="green")

# -----------------------------------------------------------

def power_cmd(a, b):
    """
    Raise a to the power of b
    Example:
    ./calCLI.py power 2 3
    """
    click.secho(f"{a} ** {b} = {power(a, b)}", fg="green")


if __name__ == "__main__":
    cli()