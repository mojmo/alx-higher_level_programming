#!/usr/bin/python3
"""
This module defines a base class 'Base' for handling shapes such as rectangles
and squares. It provides methods for serialization/deserialization to JSON and
CSV, creating instances, and drawing shapes using the Turtle graphics library.
"""
import json
import csv
import turtle


class Base:
    """
    Base class for shapes.

    Attributes:
        __nb_objects (int): Private class variable to keep track of the number
        of objects created.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor method for the Base class.

        Args:
            id (int): An optional identifier for the instance.
            If not provided, a unique ID is assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list): A list of dictionaries
            representing objects.

        Returns:
            str: JSON-formatted string.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.

        Args:
            list_objs (list): A list of objects to be serialized and saved.
        """
        with open(f"{cls.__name__}.json", "w") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON-formatted string to a list of dictionaries.

        Args:
            json_string (str): JSON-formatted string.

        Returns:
            list: A list of dictionaries representing objects.
        """

        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of the class using a dictionary of attributes.

        Args:
            **dictionary: Keyword arguments representing attributes
            of the object.

        Returns:
            Base: An instance of the class.
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy_instance = cls(2, 2)
            else:
                dummy_instance = cls(2)
            dummy_instance.update(**dictionary)
            return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Loads objects from a JSON file.

        Returns:
            list: A list of instances of the class.
        """

        try:
            with open(f"{str(cls.__name__)}.json", "r") as f:
                list_dictionaries = Base.from_json_string(f.read())
                return [cls.create(**dic) for dic in list_dictionaries]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves a list of objects to a CSV file.

        Args:
            list_objs (list): A list of objects to be serialized and saved.
        """
        with open(f"{cls.__name__}.csv", "w") as csvfile:

            if list_objs is None or len(list_objs) == 0:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]

                writer = csv.DictWriter(csvfile, fieldnames=fields)
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                writer.writeheader()
                writer.writerows(list_dictionaries)

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads objects from a CSV file.

        Returns:
            list: A list of instances of the class.
        """
        try:
            with open(f"{cls.__name__}.csv", "r", newline="") as csvfile:
                list_dictionaries = csv.DictReader(csvfile)
                list_dictionaries = [dict([key, int(val)]
                                     for key, val in dic.items())
                                     for dic in list_dictionaries]

                return [cls.create(**dic) for dic in list_dictionaries]

        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Uses Turtle graphics to draw rectangles and squares.

        Args:
            list_rectangles (list): A list of Rectangle objects to be drawn.
            list_squares (list): A list of Square objects to be drawn.
        """
        turt = turtle.Turtle()

        turt.screen.bgcolor("#b02727")
        turt.pensize(2)
        turt.shape("turtle")
        turt.color("#d68800")
        # turt.fillcolor("#d68800")

        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            # turt.begin_fill()
            for _ in range(2):
                turt.forward(90)
                turt.left(90)
                turt.forward(100)
                turt.left(90)
            # turt.end_fill()
            turt.hideturtle()

        for square in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(square.x, square.y)
            turt.down()
            # turt.begin_fill()
            for _ in range(2):
                turt.forward(square.width)
                turt.left(90)
                turt.forward(square.height)
                turt.left(90)
            # turt.end_fill()
            turt.hideturtle()

        turt.showturtle()
        turtle.exitonclick()
