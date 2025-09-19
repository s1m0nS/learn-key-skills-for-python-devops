"""
A calculator mode
"""


def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract second number from first"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide first number by second"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Raise a to the power of b"""
    return a**b
