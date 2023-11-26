#!/usr/bin/python3

"""

a module provides a function to print a square containing the character "#"

"""


def print_square(size):
    """
    Print a square made of '#' characters with the given size.

    Args:
        size (int): The size of the square. Must be a non-negative integer.

    Raises:
        TypeError: If the input `size` is not an integer.
        ValueError: If the input `size` is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
