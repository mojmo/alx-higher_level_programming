#!/usr/bin/python3
"""
This module defines a Student class.
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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to include in
            the dictionary. If None, includes all attributes. Default is None.

        Returns:
            dict: A dictionary representation of the Student instance.
        """

        if (type(attrs) is list and all(type(ele) is str for ele in attrs)):
            student_dict = {}

            for key, value in self.__dict__.items():
                if key not in attrs:
                    continue
                student_dict.update({key: value})

            return student_dict

        return self.__dict__
