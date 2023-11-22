#!/usr/bin/python3
"""magic class implementation from a bytecode"""
import math


class MagicClass:
    """magic class"""
    def __init__(self, radius=0):
        """initialize it"""
        self._MagicClass_radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass_radius = radius

    def area(self):
        """get the area"""
        return math.pi * self._MagicClass_radius**2

    def circumference(self):
        """Circumference"""
        return 2 * math.pi * self._MagicClass_radius
