#!/usr/bin/python3
"""
This module defines a class 'Square' that represents squares.
It inherits from the 'Rectangle' class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class representing squares.

    Attributes:
        __size (int): Private attribute for the size of the square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor method for creating instances of squares.

        Args:
            size (int): Size of the square.
            x (int): x-coordinate of the square (default is 0).
            y (int): y-coordinate of the square (default is 0).
            id (int): Optional identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation of a square.

        Returns:
            str: Formatted string representing the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            int: Size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Args:
            value (int): New size value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square.

        Args:
            *args: Variable number of positional arguments.
            **kwargs: Variable number of keyword arguments.
        """

        if args and len(args) != 0:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if i >= 4:
                    break
                if attrs[i] == "id" and args[i] is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    setattr(self, attrs[i], args[i])
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id" and value is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Converts the square to a dictionary representation.

        Returns:
            dict: Dictionary representing the square.
        """

        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
