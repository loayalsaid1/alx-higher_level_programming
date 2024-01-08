#!/usr/bin/python3
"""8-rectangle module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Iniitialzie the object"""
        self.__width = width
        self.__height = height

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
