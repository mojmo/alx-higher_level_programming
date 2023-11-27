#!/usr/bin/python3

"""
This module defines a Rectangle class.

The Rectangle class represents a geometric rectangle with
width and height attributes.
"""


class Rectangle:
    """A class to represent a Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle object.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
