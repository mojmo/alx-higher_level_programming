#!/usr/bin/python3
"""
This module defines a class 'Rectangle' that represents rectangles.
It inherits from the 'Base' class.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class representing rectangles.

    Attributes:
        __width (int): Private attribute for the width of the rectangle.
        __height (int): Private attribute for the height of the rectangle.
        __x (int): Private attribute for the x-coordinate of the rectangle.
        __y (int): Private attribute for the y-coordinate of the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method for creating instances of rectangles.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x-coordinate of the rectangle (default is 0).
            y (int): y-coordinate of the rectangle (default is 0).
            id (int): Optional identifier for the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        String representation of a rectangle.

        Returns:
            str: Formatted string representing the rectangle.
        """
        rect_id = f"[Rectangle] ({self.id}) "
        rect_pos = f"{self.__x}/{self.__y}"
        rect_Dimensions = f"{self.__width}/{self.__height}"
        string = rect_id + rect_pos + " - " + rect_Dimensions

        return string

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.

        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle.

        Returns:
            int: height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        Getter method for retrieving the x-coordinate of the rectangle.

        Returns:
            int: x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for setting the x-coordinate of the rectangle.

        Args:
            value (int): New x-coordinate value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Getter method for retrieving the y-coordinate of the rectangle.

        Returns:
            int: y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for setting the y-coordinate of the rectangle.

        Args:
            value (int): New y-coordinate value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the rectangle using '#' characters.
        """
        rect = ""

        for _ in range(self.__y):
            rect += "\n"

        for _ in range(self.__height):
            rect += " " * self.__x + "#" * self.__width + "\n"

        print(rect, end="")

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle.

        Args:
            *args: Variable number of positional arguments.
            **kwargs: Variable number of keyword arguments.
        """

        if args and len(args) != 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                if i >= 5:
                    break
                if attrs[i] == "id" and args[i] is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    setattr(self, attrs[i], args[i])
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id" and value is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Converts the rectangle to a dictionary representation.

        Returns:
            dict: Dictionary representing the rectangle.
        """

        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
