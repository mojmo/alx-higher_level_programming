#!/usr/bin/python3
"""
Defines the Square class, inheriting from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a specified size.

        Args:
            size (int): The size of the square.
        """

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: A string in the format "[Square] size/size".
        """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """

        return self.__size ** 2
