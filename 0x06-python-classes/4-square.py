#!/usr/bin/python3

"""Defines the Square class for representing squares."""


class Square:
    """Represents a square with a given size."""

    def __init__(self, size=0):
        """Initializes a square with the specified size.

        Args:
            size (int): The size of the square (default is 0).
        """

        self.__size = size

    @property
    def size(self):
        """Return the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set a value for the size of the square

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is a negative number.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""

        return self.__size ** 2
