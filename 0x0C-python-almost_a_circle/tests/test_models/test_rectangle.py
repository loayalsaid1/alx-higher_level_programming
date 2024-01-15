#!/usr/bin/python3
"""Test rectangle class from ../models/rectangle.py"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch


class Test_Rectangle(unittest.TestCase):
    """test Rectanlge class from rectangle module"""

    def setUp(self):
        pass

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_inheretence(self):
        self.assertTrue(isinstance(Rectangle(3, 4), Base))
        self.assertTrue(isinstance(Rectangle(3, 4), Base))

    def test_normal_case(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(2, 5, 10, 20, 4)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.length, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.id, 4)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.length, 5)
        self.assertEqual(r2.x, 10)
        self.assertEqual(r2.y, 20)

    def test_init_attrs_type_errors(self):
        message = "{} must be an integer"

        with self.assertRaises(TypeError, msg=message.format("width")):
            Rectangle("not int", 1, 1, 1)
        with self.assertRaises(TypeError, msg=message.format("length")):
            Rectangle(1, "not int", 1, 1)
        with self.assertRaises(TypeError, msg=message.format("x")):
            Rectangle(1, 1, "not int", 1)
        with self.assertRaises(TypeError, msg=message.format("y")):
            Rectangle(1, 1, 1, "not int")

    def test_setters_attrs_type_errors(self):
        r1 = Rectangle(1, 1)
        message = "{} must be an integer"

        with self.assertRaises(TypeError, msg=message.format("width")):
            r1.width = "not int"
        with self.assertRaises(TypeError, msg=message.format("length")):
            r1.length = "not int"
        with self.assertRaises(TypeError, msg=message.format("x")):
            r1.x = "not int"
        with self.assertRaises(TypeError, msg=message.format("y")):
            r1.y = "not int"

    def test_init_values_errors(self):
        message = "{} must be {} 0"

        # In inintualization
        with self.assertRaises(ValueError, msg=message.format("width", ">")):
            Rectangle(-1, 1, 1, 1)
        with self.assertRaises(ValueError, msg=message.format("length", ">")):
            Rectangle(1, -1, 1, 1)
        with self.assertRaises(ValueError, msg=message.format("x", ">=")):
            Rectangle(1, 1, -1, 1)
        with self.assertRaises(ValueError, msg=message.format("y", ">=")):
            Rectangle(1, 1, 1, -1)

    def test_setters_values_errors(self):
        message = "{} must be {} 0"
        r1 = Rectangle(1, 1)
        with self.assertRaises(ValueError, msg=message.format("width", ">")):
            r1.width = 0
        with self.assertRaises(ValueError, msg=message.format("length", ">")):
            r1.length = 0
        with self.assertRaises(ValueError, msg=message.format("x", ">=")):
            r1.x = -1
        with self.assertRaises(ValueError, msg=message.format("y", ">=")):
            r1.y = -1

    def test_private_attrs(self):
        with self.assertRaises(AttributeError):
            Rectangle(4, 5).__width
        with self.assertRaises(AttributeError):
            Rectangle(4, 5).__lenght
        with self.assertRaises(AttributeError):
            Rectangle(4, 5).__x
        with self.assertRaises(AttributeError):
            Rectangle(4, 5).__y

    def test_area(self):
        self.assertEqual(Rectangle(1, 1).area(), 1)
        self.assertEqual(Rectangle(4, 5).area(), 20)

    def test_display(self):
        with patch('builtins.print') as mock_print:
            Rectangle(1, 1).display()

            output = mock_print.mock_calls[0][1][0]
            self.assertEqual(output, '#')

        with patch('builtins.print') as mock_print:
            Rectangle(2, 3).display()

            for i in range(3):
                output = mock_print.mock_calls[i][1][0]
                self.assertEqual(output, '##')

    def test_str(self):
        """Test the output of __str__"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 5/5")
