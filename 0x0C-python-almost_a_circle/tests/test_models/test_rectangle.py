#!/usr/bin/python3
"""
This module contains a set of unit tests for the Rectangle class
in the models module.
"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInit(unittest.TestCase):
    """
    This class defines a set of unit tests for the __init__
    method in the Rectangle class
    """
    def test_constructor_noraml_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r2.id, r1.id + 1)

    def test_constructor_noraml_three_args(self):
        r1 = Rectangle(10, 2, 3)
        self.assertEqual(r1.x, 3)
        self.assertEqual(Rectangle(10, 2, 3).y, 0)

    def test_constructor_noraml_four_args(self):
        r1 = Rectangle(10, 2, 3, 9)
        self.assertEqual(r1.y, 9)

    def test_constructor_noraml_five_args(self):
        r1 = Rectangle(10, 2, 3, 9, 7)
        self.assertEqual(r1.id, 7)

    def test_constructor_noraml_six_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, 9, 7, 5)

    def test_constructor_noraml_without_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_constructor_noraml_None(self):
        with self.assertRaises(TypeError):
            Rectangle(None)

    def test_width_setter(self):
        r1 = Rectangle(10, 2, 3, 9, 7)
        r1.width = 98
        self.assertEqual(r1.width, 98)

    def test_width_getter(self):
        r1 = Rectangle(10, 2, 3, 9, 7)
        self.assertEqual(10, r1.width)

    def test_private_width(self):
        with self.assertRaises(AttributeError):
            Rectangle(10, 2, 3, 9, 7).__width

    def test_height_setter(self):
        r1 = Rectangle(10, 2, 3, 9, 7)
        r1.height = 98
        self.assertEqual(98, r1.height)

    def test_height_getter(self):
        r1 = Rectangle(10, 2, 3, 9, 7)
        self.assertEqual(2, r1.height)

    def test_private_height(self):
        with self.assertRaises(AttributeError):
            Rectangle(10, 2, 3, 9, 7).__height

    def test_x_setter(self):
        r1 = Rectangle(10, 2, 3, 9, 7)
        r1.x = 98
        self.assertEqual(98, r1.x)

    def test_x_getter(self):
        r1 = Rectangle(10, 2, 3, 9, 7)
        self.assertEqual(3, r1.x)

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            Rectangle(10, 2, 3, 9, 7).__x

    def test_y_setter(self):
        r1 = Rectangle(10, 2, 3, 9, 7)
        r1.y = 98
        self.assertEqual(98, r1.y)

    def test_y_getter(self):
        r1 = Rectangle(10, 2, 3, 9, 7)
        self.assertEqual(9, r1.y)

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            Rectangle(10, 2, 3, 9, 7).__y


class TestRectangleStr(unittest.TestCase):
    """
    This class defines a set of unit tests for the __str__
    method in the Rectangle class
    """
    def test_str_with_two_args(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 0/0 - 10/2")

    def test_str_with_three_args(self):
        r1 = Rectangle(10, 2, 3)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 3/0 - 10/2")

    def test_str_with_four_args(self):
        r1 = Rectangle(10, 2, 3, 9)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 3/9 - 10/2")

    def test_str_with_five_args(self):
        r1 = Rectangle(10, 2, 3, 9, 7)
        self.assertEqual(str(r1), f"[Rectangle] (7) 3/9 - 10/2")

    def test_str_overwrite_attributes(self):
        r1 = Rectangle(10, 2, 3, 9, 7)
        r1.width = 4
        r1.height = 5
        r1.x = 1
        r1.y = 3
        self.assertEqual(str(r1), "[Rectangle] (7) 1/3 - 4/5")

    def test_str_with_one_arg(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r1.__str__(1)


class TestRectangleWidth(unittest.TestCase):
    """
    This class defines a set of unit tests for the width
    attribute in the Rectangle class
    """

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 4)

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(3.2, 1)

    def test_width_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", 4)

    def test_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 4)

    def test_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 4)

    def test_width_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"width": 1}, 4)

    def test_width_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 4)

    def test_width_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 4)

    def test_width_frozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3}), 4)

    def test_width_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 4)

    def test_width_bytes(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'width', 4)

    def test_width_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 4)

    def test_width_negative_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('-inf'), 4)

    def test_width_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 4)

    def test_width_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 4)


class TestRectangleHeight(unittest.TestCase):
    """
    This class defines a set of unit tests for the height
    attribute in the Rectangle class
    """
    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, 0)

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, -3)

    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 3.2)

    def test_height_string(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "height")

    def test_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, [1, 2, 3])

    def test_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, (1, 2, 3))

    def test_height_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, {"height": 3})

    def test_height_bool(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, True)

    def test_height_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, {1, 2, 3})

    def test_height_frozenset(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, frozenset({1, 2, 3}))

    def test_height_range(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, range(5))

    def test_height_bytes(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, b'height')

    def test_height_inf(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, float('inf'))

    def test_height_negative_inf(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, float('-inf'))

    def test_height_nan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, float('nan'))

    def test_height_None(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, None)


class TestRectangleX(unittest.TestCase):
    """
    This class defines a set of unit tests for the x
    attribute in the Rectangle class
    """

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 3.4)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 3, -4)

    def test_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "x")

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3])

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3))

    def test_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"x": 3})

    def test_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True)

    def test_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3})

    def test_x_frozenset(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3}))

    def test_x_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def test_x_bytes(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b'X')

    def test_x_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'))

    def test_x_negative_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('-inf'))

    def test_x_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'))

    def test_x_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)


class TestRectangleY(unittest.TestCase):
    """
    This class defines a set of unit tests for the y
    attribute in the Rectangle class
    """
    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 4.5)

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 3, 4, -5)

    def test_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "y")

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, [1, 2, 3])

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, (1, 2, 3))

    def test_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {"y": 4})

    def test_y_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, True)

    def test_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {1, 2, 3})

    def test_y_frozenset(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3}))

    def test_y_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_y_bytes(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Y')

    def test_y_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, float('inf'))

    def test_y_negative_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, float('-inf'))

    def test_y_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, float('nan'))

    def test_y_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)


class TestRectangleArea(unittest.TestCase):
    """
    This class defines a set of unit tests for the area
    method in the Rectangle class
    """
    def test_area_with_small_numbers(self):
        r1 = Rectangle(5, 3, 2, 4, 98)
        self.assertEqual(r1.area(), 15)

    def test_area_with_large_numbers(self):
        r1 = Rectangle(6686987980890890, 896858578709669868, 2, 4, 98)
        self.assertEqual(r1.area(), 5997282536390448656270844428702520)

    def test_area_overwrite_args(self):
        r1 = Rectangle(5, 3, 2, 4, 98)
        r1.width = 4
        r1.height = 5
        self.assertEqual(r1.area(), 20)

    def test_area_with_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 3, 2, 4, 98).area(1)


class TestRectangleDisplay(unittest.TestCase):
    """
    This class defines a set of unit tests for the display
    method in the Rectangle class
    """
    @staticmethod
    def capture_stdout(rect):
        """
        Captures and returns the standard output generated by the 'display'
        method of a Rectangle object.

        Args:
        rect (Rectangle): A Rectangle object for which the standard output
        is to be captured.

        Returns:
        io.StringIO: A StringIO object containing the captured standard output.
        """
        capture = io.StringIO()
        sys.stdout = capture
        rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display_with_width_height(self):
        r = Rectangle(2, 3, 0, 0, 98)
        capture = TestRectangleDisplay.capture_stdout(r)
        self.assertEqual(capture.getvalue(), "##\n##\n##\n")

    def test_display_with_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 98)
        capture = TestRectangleDisplay.capture_stdout(r)
        self.assertEqual(capture.getvalue(), " ###\n ###\n")

    def test_display_with_width_height_y(self):
        r = Rectangle(4, 5, 0, 1, 98)
        capture = TestRectangleDisplay.capture_stdout(r)
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(capture.getvalue(), display)

    def test_display_with_width_height_x_y(self):
        r = Rectangle(2, 4, 3, 2, 98)
        capture = TestRectangleDisplay.capture_stdout(r)
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(capture.getvalue(), display)

    def test_display_with_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 3, 2, 98).display(1)


class TestRectangleUpdateArgs(unittest.TestCase):
    """
    This class defines a set of unit tests for the update
    method with *args as a parameter in the Rectangle class
    """

    def test_update_without_args(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (98) 3/1 - 7/5")

    def test_update_with_one_arg(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 7/5")

    def test_update_with_two_args(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/5")

    def test_update_with_three_args(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/3")

    def test_update_with_four_args(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/1 - 2/3")

    def test_update_with_five_args(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_with_six_args(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args_with_None_id(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(None)
        display = "[Rectangle] ({}) 3/1 - 7/5".format(r.id)
        self.assertEqual(str(r), display)

    def test_update_with_None_id_and_more_args(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(None, 4, 5, 2)
        display = "[Rectangle] ({}) 2/1 - 4/5".format(r.id)
        self.assertEqual(str(r), display)

    def test_update_args_twice(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 88)
        self.assertEqual(str(r), "[Rectangle] (6) 3/2 - 5/4")

    def test_update_args_invalid_width_type(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_width_zero(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_width_negative(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def test_update_args_invalid_height_type(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)

    def test_update_args_height_negative(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", 1, "invalid")

    def test_update_args_x_before_y(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "invalid", "invalid")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """
    This class defines a set of unit tests for the update
    method with **kwargs as a parameter in the Rectangle class
    """

    def test_update_kwargs_with_one_arg(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(id=66)
        self.assertEqual(str(r), "[Rectangle] (66) 3/1 - 7/5")

    def test_update_kwargs_with_two_args(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(width=3, id=66)
        self.assertEqual(str(r), "[Rectangle] (66) 3/1 - 3/5")

    def test_update_kwargs_with_three_args(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(width=3, height=3, id=66)
        self.assertEqual(str(r), "[Rectangle] (66) 3/1 - 3/3")

    def test_update_kwargs_with_four_args(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(id=66, x=5, height=2, width=4)
        self.assertEqual(str(r), "[Rectangle] (66) 5/1 - 4/2")

    def test_update_kwargs_with_five_args(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(x=8, y=7, id=66, width=4, height=2)
        self.assertEqual(str(r), "[Rectangle] (66) 8/7 - 4/2")

    def test_update_kwargs_with_six_args(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(y=7, x=8, id=66, width=4, height=2, more=87)
        self.assertEqual(str(r), "[Rectangle] (66) 8/7 - 4/2")

    def test_update_kwargs_None_id(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(id=None)
        display = "[Rectangle] ({}) 3/1 - 7/5".format(r.id)
        self.assertEqual(str(r), display)

    def test_update_kwargs_None_id_and_more(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(id=None, height=7, y=9)
        display = "[Rectangle] ({}) 3/9 - 7/7".format(r.id)
        self.assertEqual(str(r), display)

    def test_update_kwargs_twice(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=3, width=2)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 2/3")

    def test_update_args_and_kwargs(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(89, 2, height=4, y=6)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/5")

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(a=5, b=10)
        self.assertEqual(str(r), "[Rectangle] (98) 3/1 - 7/5")

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(7, 5, 3, 1, 98)
        r.update(height=5, id=66, a=1, b=54, x=19, y=7)
        self.assertEqual(str(r), "[Rectangle] (66) 19/7 - 7/5")

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="width")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-3)

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="height")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-3)

    def test_update_kwargs_inavlid_x_type(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="x")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-3)

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="y")

    def test_update_kwargs_y_negative(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-3)


class TestRectangleToDictionary(unittest.TestCase):
    """
    This class defines a set of unit tests for the to_dictionary
    method in the Rectangle class
    """

    def test_to_dictionary_normal(self):
        r = Rectangle(7, 5, 3, 1, 98)
        display = {'x': 3, 'y': 1, 'id': 98, 'height': 5, 'width': 7}
        self.assertDictEqual(display, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(7, 5, 3, 1, 98)
        r2 = Rectangle(3, 4, 4, 2, 66)
        r2.update(**r1.to_dictionary())
        self.assertFalse(r1 is r2)

    def test_to_dictionary_with_arg(self):
        r = Rectangle(7, 5, 3, 1, 98)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
