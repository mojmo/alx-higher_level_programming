#!/usr/bin/python3
"""
Defines the BaseGeometry and Rectangle classes.
"""


class BaseGeometry:
    """
    A base class for geometry-related operations.
    """
    def area(self):
        """
        Placeholder method for calculating the area of a geometry.
        This method is meant to be overridden in derived classes.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is an integer greater than 0.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with a specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """

        super().__init__()
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
