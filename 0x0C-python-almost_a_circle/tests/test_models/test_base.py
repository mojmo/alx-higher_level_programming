#!/usr/bin/python3
"""
This module contains unit tests for the Base class in the models module.
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInit(unittest.TestCase):
    """
    This class defines a set of unit tests for the initialization of the Base
    class in the models module. The tests cover various scenarios related to
    instance creation, ID management, and attribute access.
    Each test case validates the expected behavior of the Base class in
    different initialization scenarios.
    """

    def test_instance_creation_with_id(self):
        obj = Base(34)
        self.assertEqual(obj.id, 34)

    def test_instance_creation_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, obj2.id - 1)
        self.assertEqual(obj2.id, obj1.id + 1)

    def test_instance_creation_two_args(self):
        with self.assertRaises(TypeError):
            print(Base(1, 2).id)

    def test_instance_creation_three_args(self):
        with self.assertRaises(TypeError):
            print(Base(1, 2, 4).id)

    def test_instance_creation_with_None(self):
        obj1 = Base(None)
        obj2 = Base(None)
        self.assertEqual(obj1.id, obj2.id - 1)
        self.assertEqual(obj2.id, obj1.id + 1)

    def test_nb_instances_with_id(self):
        obj1 = Base()
        obj2 = Base(98)
        obj3 = Base()
        self.assertEqual(obj1.id, obj3.id - 1)
        self.assertEqual(obj3.id, obj1.id + 1)
        self.assertEqual(obj2.id, 98)

    def test_to_change_id(self):
        obj = Base(98)
        obj.id = 32
        self.assertEqual(obj.id, 32)

    def test_to_access_nb_instances(self):
        obj1 = Base()
        obj2 = Base()
        with self.assertRaises(AttributeError):
            print(Base().__nb_instances)

    def test_string_id(self):
        obj = Base("id")
        self.assertEqual(obj.id, "id")

    def test_list_id(self):
        obj = Base([1, 2, 3])
        self.assertEqual(obj.id, [1, 2, 3])

    def test_tuple_id(self):
        obj = Base((1, 2))
        self.assertEqual(obj.id, (1, 2))

    def test_dict_id(self):
        obj = Base({"id": 3})
        self.assertEqual(obj.id, {"id": 3})

    def test_float_id(self):
        obj = Base(8.3)
        self.assertEqual(obj.id, 8.3)

    def test_boolean_id(self):
        obj = Base(True)
        self.assertEqual(obj.id, True)

    def test_inf_id(self):
        obj = Base(float('inf'))
        self.assertEqual(obj.id, float('inf'))

    def test_negative_inf_id(self):
        obj = Base(float('-inf'))
        self.assertEqual(obj.id, float('-inf'))

    def test_nan_id(self):
        obj = Base(float('nan'))
        self.assertNotEqual(obj.id, float('nan'))


class TestBaseToJsonString(unittest.TestCase):
    """
    This class defines a set of unit tests for the to_json_string method in
    the Base class of the models module. The tests cover scenarios involving
    Rectangle and Square instances, including conversion to dictionaries
    and JSON strings.
    """
    def test_rect_instance(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)

    def test_rect_instance_two(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(12, 2, 3, 1)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertEqual(type(Base.to_json_string(list_dicts)), str)

    def test_square_instance(self):
        s1 = Square(1, 4, 2, 2)
        self.assertEqual(type(Base.to_json_string([s1.to_dictionary()])), str)

    def test_square_instance_two(self):
        s1 = Square(10, 4, 2, 8)
        s2 = Square(12, 2, 3, 1)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertEqual(type(Base.to_json_string(list_dicts)), str)

    def test_empty_list(self):
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")

    def test_None_list(self):
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_no_args_passed(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_two_args_passed(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([{"width": 2}], 98)


class TestBaseSaveToFile(unittest.TestCase):
    """
    This class defines a set of unit tests for the save_to_file method
    in the Base class and its derived classes (Rectangle and Square) of
    the models module. The tests cover scenarios related to saving object
    data to JSON files and handling different inputs.
    """

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("Base.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_to_file_with_list_of_objects_base(self):
        obj1 = Rectangle(10, 8, 7, 2, 9)
        Base.save_to_file([obj1])
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertIn('"id": 9', content)

    def test_save_to_file_with_list_of_objects(self):
        obj1 = Rectangle(10, 2, 7, 2, 8)
        obj2 = Rectangle(13, 5, 4, 5, 1)
        Rectangle.save_to_file([obj1, obj2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertIn('"id": 8', content)
            self.assertIn('"id": 1', content)

    def test_save_to_file_with_list_of_objects_sq(self):
        obj1 = Square(2, 7, 2, 8)
        obj2 = Square(5, 4, 5, 1)
        Square.save_to_file([obj1, obj2])
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertIn('"id": 8', content)
            self.assertIn('"id": 1', content)

    def test_save_to_file_with_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_with_empty_list_sq(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_with_None_list(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_overwrite(self):
        obj1 = Rectangle(10, 2, 7, 2, 8)
        Rectangle.save_to_file([obj1])
        obj1 = Rectangle(13, 5, 4, 5, 1)
        Rectangle.save_to_file([obj1])
        with open("Rectangle.json", "r") as f:
            self.assertIn('"id": 1', f.read())

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_None_list(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_without_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_with_two_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 98)


class TestBaseFromJsonString(unittest.TestCase):
    """
    This class defines a set of unit tests for the from_json_string
    method in the Base class
    """
    def test_normal_json_string(self):
        json_list_input = Rectangle.to_json_string([
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ])
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)

    def test_normal_json_string_sq(self):
        json_list_input = Square.to_json_string([
            {'id': 89, 'size': 10, 'x': 4, 'y': 2},
            {'id': 7, 'size': 1, 'x': 7, 'y': 9}
        ])
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)

    def test_empty_list(self):
        list_output = Rectangle.from_json_string('[]')
        self.assertEqual(type('[]'), str)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_output, [])

    def test_None_list(self):
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_output, [])

    def test_no_args_passed(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Rectangle.from_json_string("[{'id': 2}]", "[{'width': 4}]")


class TestBaseCreate(unittest.TestCase):
    """
    This class defines a set of unit tests for the create()
    method in the Base class
    """

    def test_create_instance_with_valid_dictionary(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r2.width, 3)

    def test_create_instance_with_valid_dictionary_rect_str(self):
        r1 = Rectangle(3, 5, 1, 9, 98)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (98) 1/9 - 3/5", str(r2))

    def test_create_instances_not_equals(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_create_instance_with_valid_dictionary_sq(self):
        r1 = Square(3, 5, 1, 20)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(r2.size, 3)

    def test_create_instance_with_valid_dictionary_sq_str(self):
        r1 = Square(3, 1, 9, 98)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual("[Square] (98) 1/9 - 3", str(r2))

    def test_create_instance_sq_not_equals(self):
        r1 = Square(3, 5, 1, 20)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_create_instance_with_empty_dictionary(self):
        with self.assertRaises(TypeError):
            Base.create({})

    def test_create_instance_with_empty_args(self):
        obj = Base.create()
        self.assertEqual(obj, None)


class TestBaseLoadFromFile(unittest.TestCase):
    """
    This class defines a set of unit tests for the load_from_file
    method in the Base class
    """

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("Base.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_normal_rect(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(type(list_rectangles_output), list)
        self.assertEqual(list_rectangles_output[0].width, 10)

    def test_load_from_file_normal_sq(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(type(list_squares_output), list)
        self.assertEqual(list_squares_output[1].size, 7)

    def test_load_from_file_rect_types(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) is Rectangle
                            for obj in list_rectangles_output))

    def test_load_from_file_sq_types(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertTrue(all(type(obj) is Square
                            for obj in list_squares_output))

    def test_load_from_file_with_nonexistent_file(self):
        loaded_objs = Rectangle.load_from_file()
        self.assertEqual(loaded_objs, [])

    def test_load_from_file_with_two_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 98)


class TestBaseSaveToFileCsv(unittest.TestCase):
    """
    This class defines a set of unit tests for the save_to_file_csv
    method in the Base class
    """

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("Base.csv")
        except IOError:
            pass
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_save_to_csv_file_rect(self):
        r1 = Rectangle(10, 7, 2, 8, 98)
        r2 = Rectangle(2, 4, 9, 21, 88)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as file:
            content = file.read()
            self.assertTrue("10,7,2,8,98\n2,4,9,21,88", content)

    def test_save_to_csv_file_sq(self):
        s1 = Square(5, 1, 7, 98)
        s2 = Square(7, 9, 1, 88)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as file:
            content = file.read()
            self.assertTrue("5,1,7,98\n7,9,1,88", content)

    def test_save_to_csv_file_base(self):
        s1 = Square(5, 1, 7, 98)
        Base.save_to_file_csv([s1])
        with open("Base.csv", "r") as file:
            self.assertTrue("98,5,1,7", file.read())

    def test_save_to_csv_file_overwrite(self):
        s1 = Square(5, 1, 7, 98)
        Square.save_to_file_csv([s1])
        s1 = Square(7, 9, 1, 88)
        Square.save_to_file_csv([s1])
        with open("Square.csv", "r") as file:
            self.assertTrue("88,7,9,1", file.read())

    def test_save_to_file_csv_empty_list(self):
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_csv_file_none_arg(self):
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_csv_no_args_passed(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_with_two_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 98)


class TestBaseLoadFromFileCsv(unittest.TestCase):
    """
    This class defines a set of unit tests for the load_from_File_csv
    method in the Base class
    """

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("Base.csv")
        except IOError:
            pass
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_csv_file_normal_rect(self):
        r1 = Rectangle(10, 7, 2, 8, 98)
        r2 = Rectangle(2, 4, 9, 21, 88)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(list_rectangles_output[0]), str(r1))

    def test_load_from_file_normal_sq(self):
        s1 = Square(5, 1, 7, 98)
        s2 = Square(7, 9, 1, 88)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(list_squares_output[1]), str(s2))

    def test_load_from_csv_file_rect_types(self):
        r1 = Rectangle(10, 7, 2, 8, 98)
        r2 = Rectangle(2, 4, 9, 21, 88)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) is Rectangle
                            for obj in list_rectangles_output))

    def test_load_from_csv_file_sq_types(self):
        s1 = Square(5, 1, 7, 98)
        s2 = Square(7, 9, 1, 88)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) is Square
                            for obj in list_squares_output))

    def test_load_from_csv_file_with_nonexistent_file(self):
        loaded_objs = Rectangle.load_from_file_csv()
        self.assertEqual(loaded_objs, [])

    def test_load_from_csv_file_with_two_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 98)


if __name__ == "__main__":
    unittest.main()
