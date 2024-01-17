#!/usr/bin/python3
"""TEst models.square modlue"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_square(unittest.TestCase):
    """test square class"""
    def tearDown(self):
        """Tear down"""
        Base._Base__nb_objects = 0

    def test_inheritence(self):
        """test if square is a subclass of Rectangle"""
        self.assertIsInstance(Square(3), Rectangle)

    def test_instantiation(self):
        """test instantiation"""
        s1 = Square(12)
        s2 = Square(14, 1, 1, 40)

        self.assertEqual(s1.size, 12)
        self.assertEqual(s1.height, 12)
        self.assertEqual(s1.width, 12)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

        self.assertEqual(s2.size, 14)
        self.assertEqual(s2.height, 14)
        self.assertEqual(s2.width, 14)
        self.assertEqual(s2.x, 1)
        self.assertEqual(s2.y, 1)
        self.assertEqual(s2.id, 40)

    def test_size_bad_input(self):
        """test bad input for size"""
        s1 = Square(3)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square("3")

        with self.assertRaises(ValueError, msg="width must be > 0"):
            Square(-4)

    def test_str(self):
        """test str overriding"""
        s1 = Square(4)

        form = "[Square] (1) 0/0 - 4"
        self.assertEqual(s1.__str__(), form)

    def test_size_change(self):
        """test size setters and getters"""
        s1 = Square(4)

        s1.size = 3
        self.assertEqual(s1.size, 3)
        self.assertEqual([s1.size, s1.width, s1.height], [3, 3, 3])

    def test_size_setter_bad_input(self):
        """test bad input for size"""
        s1 = Square(3)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            s1.size = "not int"

        with self.assertRaises(ValueError, msg="width must be > 0"):
            s1.size = -3

    def test_update(self):
        """Update test"""
        s1 = Square(10, 2, 4)
        self.assertEqual(str(s1), "[Square] (1) 2/4 - 10")
        s1.update()
        self.assertEqual(str(s1), "[Square] (1) 2/4 - 10")
        s1.update(89)
        self.assertEqual(str(s1), "[Square] (89) 2/4 - 10")
        s1.update(89, 2)
        self.assertEqual(str(s1), "[Square] (89) 2/4 - 2")
        s1.update(89, 2, 3)
        self.assertEqual(str(s1), "[Square] (89) 3/4 - 2")
        s1.update(89, 2, 3, 5)
        self.assertEqual(str(s1), "[Square] (89) 3/5 - 2")
        s1.update(89, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (89) 3/4 - 2")

    def test_update_kwargs(self):
        """test update function when passing kwargs"""
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(str(s1), "[Square] (10) 10/10 - 10")
        s1.update(id=3)
        self.assertEqual(str(s1), "[Square] (3) 10/10 - 10")
        s1.update(89, id=4)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 10")
        s1.update()
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 10")
        s1.update(y=10, x=20, id=90, size=9)
        self.assertEqual(str(s1), "[Square] (90) 20/10 - 9")
        s1.update(id=50, size=3, x=4, y=5)
        self.assertEqual(str(s1), "[Square] (50) 4/5 - 3")


