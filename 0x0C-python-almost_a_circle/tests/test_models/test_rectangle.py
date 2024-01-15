#!/usr/bin/python3
"""Test rectangle class from ../models/rectangle.py"""


import unittest
from models.base import Base
from  models.rectangle import Rectangle

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
        r2 = Rectangle(2.5, 5.5, 10, 20, 4)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.length, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.id, 4)
        self.assertEqual(r2.width, 2.5)
        self.assertEqual(r2.length, 5.5)
        self.assertEqual(r2.x, 10)
        self.assertEqual(r2.y, 20)


    def test_private_attrs(self):
        with self.assertRaises(AttributeError):
            Rectangle(4, 5).__width
            Rectangle(4, 5).__lenght
            Rectangle(4, 5).__x
            Rectangle(4, 5).__y
