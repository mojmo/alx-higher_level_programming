#!/usr/bin/python3
"""
This module contains a set of unit tests for the Square class
in the models module.
"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInit(unittest.TestCase):
    """
    This class defines a set of unit tests for the __init__
    method in the Square class
    """

    def test_square_inherets_from_base(self):
        self.assertIsInstance(Square(5), Base)

    def test_square_inherets_from_rectangle(self):
        self.assertIsInstance(Square(5), Rectangle)

    def test_init_with_one_arg(self):
        s1 = Square(5)
        s2 = Square(4)
        self.assertEqual(s1.id, s2.id - 1)

    def test_init_with_two_args(self):
        s1 = Square(5, 2)
        s2 = Square(2, 2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_init_with_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_init_with_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_init_with_five_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_init_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_private_size(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_setter(self):
        s = Square(5, 3, 1, 2)
        s.size = 7
        self.assertEqual(7, s.size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 3, 1, 2).size)

    def test_width_getter(self):
        s = Square(5, 3, 1, 2)
        s.size = 7
        self.assertEqual(7, s.width)

    def test_height_getter(self):
        s = Square(5, 3, 1, 2)
        s.size = 7
        self.assertEqual(7, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(5).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(5).y)


class TestSquareStr(unittest.TestCase):
    """
    This class defines a set of unit tests for the __str__
    method in the Square class
    """
    def test_str_with_two_args(self):
        s1 = Square(10, 2)
        self.assertEqual(str(s1), f"[Square] ({s1.id}) 2/0 - 10")

    def test_str_with_three_args(self):
        s1 = Square(10, 2, 3)
        self.assertEqual(str(s1), f"[Square] ({s1.id}) 2/3 - 10")

    def test_str_with_four_args(self):
        s1 = Square(10, 2, 3, 7)
        self.assertEqual(str(s1), f"[Square] (7) 2/3 - 10")

    def test_str_with_five_args(self):
        s1 = Square(10, 2, 3, 7)
        self.assertEqual(str(s1), f"[Square] (7) 2/3 - 10")

    def test_str_overwrite_attributes(self):
        s1 = Square(10, 2, 3, 7)
        s1.size = 5
        s1.x = 1
        s1.y = 4
        self.assertEqual(str(s1), "[Square] (7) 1/4 - 5")

    def test_str_with_one_arg(self):
        s1 = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s1.__str__(1)


class TestSquareSize(unittest.TestCase):
    """
    This class defines a set of unit tests for the size
    attribute in the Square class
    """
    def test_size_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 4)

    def test_size_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-3, 4)

    def test_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(3.2, 1)

    def test_size_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("width", 4)

    def test_size_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3], 4)

    def test_size_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 4)

    def test_size_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"width": 1}, 4)

    def test_size_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 4)

    def test_size_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 4)

    def test_size_frozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3}), 4)

    def test_size_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5), 4)

    def test_size_bytes(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'width', 4)

    def test_size_bytearray(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcdefg'))

    def test_size_memoryview(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcdefg'))

    def test_size_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_size_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'), 4)

    def test_size_negative_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('-inf'), 4)

    def test_size_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'), 4)

    def test_size_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 4)


class TestSquareX(unittest.TestCase):
    """
    This class defines a set of unit tests for the x
    attribute in the Square class
    """

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 3.4)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(3, -4)

    def test_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "x")

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, [1, 2, 3])

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, (1, 2, 3))

    def test_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {"x": 3})

    def test_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, True)

    def test_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {1, 2, 3})

    def test_x_frozenset(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, frozenset({1, 2, 3}))

    def test_x_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, range(5))

    def test_x_bytes(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, b'X')

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'abcedfg'))

    def test_x_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, float('inf'))

    def test_x_negative_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, float('-inf'))

    def test_x_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, float('nan'))

    def test_x_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, None)


class TestSquareY(unittest.TestCase):
    """
    This class defines a set of unit tests for the y
    attribute in the Square class
    """

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, 4.5)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 4, -5)

    def test_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, "y")

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, [1, 2, 3])

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, (1, 2, 3))

    def test_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, {"y": 4})

    def test_y_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, True)

    def test_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, {1, 2, 3})

    def test_y_frozenset(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, frozenset({1, 2, 3}))

    def test_y_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, range(5))

    def test_y_bytes(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, b'Y')

    def test_y_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, complex(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, b'Hello')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, bytearray(b'Hello'))

    def test_y_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, float('inf'))

    def test_y_negative_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, float('-inf'))

    def test_y_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, float('nan'))

    def test_y_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, None)


class TestSquareArea(unittest.TestCase):
    """
    This class defines a set of unit tests for the area
    method in the Square class
    """
    def test_area_with_small_numbers(self):
        s = Square(5, 2, 4, 98)
        self.assertEqual(s.area(), 25)

    def test_area_with_large_numbers(self):
        s = Square(6686987980890890, 2, 4, 98)
        self.assertEqual(s.area(), 44715808256579221843798084992100)

    def test_area_overwrite_args(self):
        s = Square(2, 2, 4, 98)
        s.size = 5
        self.assertEqual(s.area(), 25)

    def test_area_with_one_arg(self):
        with self.assertRaises(TypeError):
            Square(5, 3, 2, 4, 98).area(1)


class TestSquareDisplay(unittest.TestCase):
    """
    This class defines a set of unit tests for the display
    method in the Square class
    """

    @staticmethod
    def capture_stdout(sq):
        """
        Captures and returns the standard output generated by the 'display'
        method of a Square object.

        Args:
        sq (Square): A Square object for which the standard output
        is to be captured.

        Returns:
        io.StringIO: A StringIO object containing the captured standard output.
        """
        capture = io.StringIO()
        sys.stdout = capture
        sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display_with_width_height(self):
        s = Square(3, 0, 0, 98)
        capture = TestSquareDisplay.capture_stdout(s)
        self.assertEqual(capture.getvalue(), "###\n###\n###\n")

    def test_display_with_width_height_x(self):
        s = Square(2, 1, 0, 98)
        capture = TestSquareDisplay.capture_stdout(s)
        self.assertEqual(capture.getvalue(), " ##\n ##\n")

    def test_display_with_width_height_y(self):
        s = Square(4, 0, 1, 98)
        capture = TestSquareDisplay.capture_stdout(s)
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(capture.getvalue(), display)

    def test_display_with_width_height_x_y(self):
        s = Square(2, 3, 2, 98)
        capture = TestSquareDisplay.capture_stdout(s)
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(capture.getvalue(), display)

    def test_display_with_one_arg(self):
        with self.assertRaises(TypeError):
            Square(4, 3, 2, 98).display(1)


class TestSquareUpdateArgs(unittest.TestCase):
    """
    This class defines a set of unit tests for the update
    method with *args as a parameter in the Square class
    """

    def test_update_without_args(self):
        s = Square(7, 3, 1, 98)
        s.update()
        self.assertEqual(str(s), "[Square] (98) 3/1 - 7")

    def test_update_with_one_arg(self):
        s = Square(7, 3, 1, 98)
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 3/1 - 7")

    def test_update_with_two_args(self):
        s = Square(7, 3, 1, 98)
        s.update(89, 2)
        self.assertEqual(str(s), "[Square] (89) 3/1 - 2")

    def test_update_with_three_args(self):
        s = Square(7, 3, 1, 98)
        s.update(89, 2, 4)
        self.assertEqual(str(s), "[Square] (89) 4/1 - 2")

    def test_update_with_four_args(self):
        s = Square(7, 3, 1, 98)
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")

    def test_update_with_five_args(self):
        s = Square(7, 3, 1, 98)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")

    def test_update_args_with_None_id(self):
        s = Square(7, 3, 1, 98)
        s.update(None)
        display = "[Square] ({}) 3/1 - 7".format(s.id)
        self.assertEqual(str(s), display)

    def test_update_with_None_id_and_more_args(self):
        s = Square(7, 3, 1, 98)
        s.update(None, 4, 5, 2)
        display = "[Square] ({}) 5/2 - 4".format(s.id)
        self.assertEqual(str(s), display)

    def test_update_args_twice(self):
        s = Square(7, 3, 1, 98)
        s.update(89, 2, 3, 4, 5, 6)
        s.update(6, 5, 4, 3, 2, 88)
        self.assertEqual(str(s), "[Square] (6) 4/3 - 5")

    def test_update_args_invalid_size_type(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid")

    def test_update_args_size_zero(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0)

    def test_update_args_size_negative(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, -4)

    def test_update_args_invalid_x(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid")

    def test_update_args_x_negative(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(98, 1, -4)

    def test_update_args_invalid_y(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 1, 2, "invalid")

    def test_update_args_y_negative(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(98, 1, 2, -4)

    def test_update_args_size_before_x(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid", "invalid")


class TestSquareUpdateKwargs(unittest.TestCase):
    """
    This class defines a set of unit tests for the update
    method with **kwargs as a parameter in the Square class
    """

    def test_update_kwargs_with_one_arg(self):
        s = Square(7, 3, 1, 98)
        s.update(id=1)
        self.assertEqual(str(s), "[Square] (1) 3/1 - 7")

    def test_update_kwargs_with_two_args(self):
        s = Square(7, 3, 1, 98)
        s.update(size=1, id=2)
        self.assertEqual(str(s), "[Square] (2) 3/1 - 1")

    def test_update_kwargs_with_three_args(self):
        s = Square(7, 3, 1, 98)
        s.update(y=5, size=3, id=66)
        self.assertEqual(str(s), "[Square] (66) 3/5 - 3")

    def test_update_kwargs_with_four_args(self):
        s = Square(7, 3, 1, 98)
        s.update(id=66, x=3, y=5, size=4)
        self.assertEqual(str(s), "[Square] (66) 3/5 - 4")

    def test_update_kwargs_width_setter(self):
        s = Square(7, 3, 1, 98)
        s.update(id=89, size=5)
        self.assertEqual(5, s.width)

    def test_update_kwargs_height_setter(self):
        s = Square(7, 3, 1, 98)
        s.update(id=89, size=6)
        self.assertEqual(6, s.height)

    def test_update_kwargs_None_id(self):
        s = Square(7, 3, 1, 98)
        s.update(id=None)
        display = "[Square] ({}) 3/1 - 7".format(s.id)
        self.assertEqual(str(s), display)

    def test_update_kwargs_None_id_and_more(self):
        s = Square(7, 3, 1, 98)
        s.update(id=None, size=4, x=10)
        display = "[Square] ({}) 10/1 - 4".format(s.id)
        self.assertEqual(str(s), display)

    def test_update_kwargs_twice(self):
        s = Square(7, 3, 1, 98)
        s.update(id=66, x=1)
        s.update(y=8, x=7, size=2)
        self.assertEqual(str(s), "[Square] (66) 7/8 - 2")

    def test_update_args_and_kwargs(self):
        s = Square(7, 3, 1, 98)
        s.update(66, 2, y=6)
        self.assertEqual(str(s), "[Square] (66) 3/1 - 2")

    def test_update_kwargs_wrong_keys(self):
        s = Square(7, 3, 1, 98)
        s.update(a=5, b=10)
        self.assertEqual(str(s), "[Square] (98) 3/1 - 7")

    def test_update_kwargs_some_wrong_keys(self):
        s = Square(7, 3, 1, 98)
        s.update(size=5, id=66, a=1, b=54)
        self.assertEqual(str(s), "[Square] (66) 3/1 - 5")

    def test_update_kwargs_invalid_size(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negative(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-5)

    def test_update_kwargs_invalid_x(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-3)

    def test_update_kwargs_invalid_y(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-3)


class TestSquareToDictionary(unittest.TestCase):
    """
    This class defines a set of unit tests for the to_dictionary
    method in the Square class
    """
    def test_to_dictionary_normal(self):
        s = Square(7, 3, 1, 98)
        display = {'id': 98, 'x': 3, 'size': 7, 'y': 1}
        self.assertDictEqual(display, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        s1 = Square(7, 3, 1, 98)
        s2 = Square(3, 4, 2, 66)
        s2.update(**s1.to_dictionary())
        self.assertFalse(s1 is s2)

    def test_to_dictionary_with_arg(self):
        s = Square(7, 3, 1, 98)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


class TestSquareOrderOfParameters(unittest.TestCase):
    """Unittests for testing order of Square attribute initialization."""

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")


if __name__ == "__main__":
    unittest.main()
