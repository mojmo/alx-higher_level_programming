#!/usr/bin/python3

"""Defines the Square class for representing squares."""


class Square:
    """Represents a square with a given size."""

    def __init__(self, size=0):
        """Initializes a square with the specified size.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is a negative number.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size