#!/usr/bin/python3
"""Tests for Base.py module"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from json import loads, dumps


class Test_Base(unittest.TestCase):
    """Test Base class"""
    def setUp(self):
        """set up"""
        pass

    def tearDown(self):
        """tear down"""
        Base._Base__nb_objects = 0

    def test_init(self):
        """test init"""
        b1 = Base()
        b2 = Base()
        b3 = Base(30)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 30)

    def test_to_json(self):
        """test Json repreesntation of multible objects"""
        pass
