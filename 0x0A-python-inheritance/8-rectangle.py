#!/usr/bin/python3
"""
Defines the BaseGeometry and Rectangle classes.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
