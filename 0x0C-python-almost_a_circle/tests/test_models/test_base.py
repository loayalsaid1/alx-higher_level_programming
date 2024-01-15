#!/usr/bin/python3
"""Tests for Base.py module"""


import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """Test Base class"""
    def test_init(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(30)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 30)
