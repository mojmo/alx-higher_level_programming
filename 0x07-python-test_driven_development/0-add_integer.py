#!/usr/bin/python3

"""

A module includes a function for adding two numbers.

"""


def add_integer(a, b=98):
    """Add two numbers

    Args:
        a: The first number
        b: The second number (Defaults to 98)

    Returns:
        The result of adding the two numbers

    Raises:
        TypeError: if one of the numbers isn't an integer or float

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
