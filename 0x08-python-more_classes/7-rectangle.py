#!/usr/bin/python3

"""
This module defines a Rectangle class.

The Rectangle class represents a geometric rectangle with width
and height attributes and area() and perimeter() methods.
"""


class Rectangle:
    """A class to represent a Rectangle

    Attributes:
        number_of_instances (int): A class attribute that counts the
        number of Rectangle instances.
        print_symbol: The symbol used for representing the rectangle
        units in the string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle object.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle,
            where 'print_symbol' represents each unit of area.
        """

        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect

        for _ in range(0, self.__height):
            rect += str(self.print_symbol) * self.__width + "\n"

        return rect[:-1]

    def __repr__(self):
        """Return a string representation of the Rectangle object.

        Returns:
            str: A string representation of the Rectangle object
            in the format 'Rectangle(width, height)'.
        """

        rect = f"Rectangle({self.__width}, {self.__height})"
        return rect

    def __del__(self):
        """Destructor method for the Rectangle object with a message."""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """

        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)
