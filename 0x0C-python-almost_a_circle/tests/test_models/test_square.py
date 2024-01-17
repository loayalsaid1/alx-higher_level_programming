#!/usr/bin/python3
"""TEst models.square modlue"""


import unittest
from models.rectangle import Rectangle
from models.square import Square


class Test_square(unittest.TestCase):
    """test square class"""
    def test_inheritence(self):
        """test if square is a subclass of Rectangle"""
        self.assertIsInstance(Square(3), Rectangle)
    
    def test_instantiation(self):
        """test instantiation"""
        r1 = Square(3)
        r2 = Square(4, 1, 1, 40)

        self.assertEqual(r1.size, 3)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        self.assertEqual(r2.size, 4)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 1)
        self.assertEqual(r2.id, 40)
    
    def test_str(self):
        """test str overriding"""
        r1 = Square(4)

        form = "[Square] (1) 0/0 1"
        self.assertEqual(r1.__str__(), form)

        
