#!/usr/bin/python3
"""1-square.py module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from rectangle"""
    def __init__(self, size):
        """init the object"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """implement area"""
        return super().area()

    def __str__(self):
        """IMPLEMENT THE STR REPRESENTATION OF AN OBJECT"""
        return f"[Square] {self.__size}/{self.__size}"
