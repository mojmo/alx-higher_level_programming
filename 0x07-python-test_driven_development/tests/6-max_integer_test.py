#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit testing for max_integer module
    """

    def test_max_integer_at_beg(self):
        self.assertEqual(max_integer([87, -4, 36, 52]), 87)

    def test_max_integer_at_mid(self):
        self.assertEqual(max_integer([-4, 36, 87, 2, 52]), 87)

    def test_max_integer_at_end(self):
        self.assertEqual(max_integer([-4, 36, 52, 87]), 87)

    def test_float_max_integer(self):
        self.assertEqual(max_integer([-4.1, 87.2, 36.0, 165.3, 13]), 165.3)

    def test_max_integer_zero(self):
        self.assertEqual(max_integer([0, 0.0]), 0)

    def test_negative_nmubers(self):
        self.assertEqual(max_integer([-4, -82, -1, -73]), -1)

    def test_one_element(self):
        self.assertEqual(max_integer([87]), 87)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_no_param(self):
        self.assertEqual(max_integer(), None)

    def test_nan(self):
        self.assertEqual(max_integer([-4, 87, float('nan'), 98, 52]), 98)

    def test_large_integers(self):
        self.assertEqual(max_integer([
            4587768, -6543567, 76543245, 86757,
            987654323, 543245, 88647, 82, 7228, 91, 4]), 987654323)

    def test_large_floats(self):
        self.assertEqual(max_integer([
            9689.76543, 654.3567, 765432.45, -86.757,
            9.87654323, 54.3245, 8864.7, 82.0, 7228, 91, 4.22]), 765432.45)

    def test_num_without_list(self):
        with self.assertRaises(TypeError):
            max_integer(98)

    def test_str_list(self):
        with self.assertRaises(TypeError):
            max_integer([-4, 87, "36", 52])

    def test_list_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([2, 5, 234, [23, 78], 133])

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)
