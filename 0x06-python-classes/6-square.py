#!/usr/bin/python3

"""Defines the Square class for representing squares."""


class Square:
    """Represents a square with a given size."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with the specified size and position.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position.
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the position"""

        return self.__position

    @position.setter
    def position(self, value):
        """Set the position

        Args:
            value (tuple): a tuple of 2 positive integers.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""

        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""

        if (self.__size == 0):
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
