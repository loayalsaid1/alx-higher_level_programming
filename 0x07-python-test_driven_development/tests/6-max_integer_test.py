#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for max_integer function"""
    def test_mod_docs(self):
        """test module docsting"""
        docs = __import__('6-max_integer').__doc__
        self.assertTrue(len(docs) > 1)

    def test_func_docs(self):
        """Test function docs"""
        docs = max_integer.__doc__
        self.assertTrue(len(docs) > 1)

    def test_no_args(self):
        """Test when passing no args"""
        self.assertIsNone(max_integer())

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_value(self):
        """Test a list with one elemnt"""
        self.assertEqual(max_integer([3]), 3)

    def test_multible_positives(self):
        """Test a list of positive numbers"""
        self.assertEqual(max_integer([0, 5, 9]), 9)

    def test_starting_max(self):
        """Test a list of positive numbers with max at start"""
        self.assertEqual(max_integer([10, 5, 9]), 10)

    def test_negatives(self):
        """test a list of negative numbers"""
        self.assertEqual(max_integer([-10, -4, -20, -9, -2, -7]), -2)

    def test_equals(self):
        """test a list of equal numbers"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_args(self):
        """Tests for a non-int type in list"""
        with self.assertRaises(TypeError):
            max_integer([1, "2", "Hi", 4])


if __name__ == "__main__":
    unittest.main()
