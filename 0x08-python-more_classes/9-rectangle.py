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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the larger area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: if either rect_1 or rect_2 is not
            an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the larger area.
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a square Rectangle instance.

        Args:
            size (int): The size of the square. Defaults to 0.

        Returns:
            Rectangle: A new Rectangle instance representing a square.
        """

        return Rectangle(size, size)
