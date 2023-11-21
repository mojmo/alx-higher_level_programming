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

    def __eq__(self, other):
        """
        Compare two objects based on their areas for equality.

        Args:
            self: The first object.
            other: The second object.

        Returns:
            True if the area of the first object is equal to the area
            of the second object, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare two objects based on their areas for inequality.

        Args:
            self: The first object.
            other: The second object.

        Returns:
            True if the area of the first object is not equal to the area
            of the second object, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compare two objects based on their areas for less than.

        Args:
            self: The first object.
            other: The second object.

        Returns:
            True if the area of the first object is less than the area
            of the second object, False otherwise.
    """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare two objects based on their areas for less than or equal to.

        Args:
            self: The first object.
            other: The second object.

        Returns:
            True if the area of the first object is less than or equal to
            the area of the second object, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compare two objects based on their areas for greater than.

        Args:
            self: The first object.
            other: The second object.

        Returns:
            True if the area of the first object is greater than the area
            of the second object, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare two objects based on their areas for greater than or equal to.

        Args:
            self: The first object.
            other: The second object.

        Returns:
            True if the area of the first object is greater than or equal to
            the area of the second object, False otherwise.
        """
        return self.area() >= other.area()

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
