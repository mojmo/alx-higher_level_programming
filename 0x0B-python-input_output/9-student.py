#!/usr/bin/python3
"""
This module defines a Student class and a method for converting
an instance to a JSON-formatted dictionary.
"""


class Student:
    """
    Represents a student with attributes first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts the Student instance to a JSON-formatted dictionary.

        Returns:
            dict: A dictionary representation of the Student instance.
        """

        return self.__dict__
