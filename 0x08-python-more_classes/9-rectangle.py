#!/usr/bin/python3
""" Module to represent a rectangle and operations on it"""


class Rectangle:
    """
    A class to represent a rectangle and operations one it
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize the class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """A setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """A setter for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """
        Return the perimeter of it: (<width> + <height>) * 2
        in case any of the width or the heigth is zero, return 0
        """
        if self.width and self.height:
            return 2 * (self.width + self.height)
        else:
            return 0

    def area(self):
        """Return the area of it, <width> * <height>"""
        return self.width * self.height

    def __str__(self):
        """Represent the string representation of the rectnalge
        with class attribute <print_symbol>

        ***** NOTE *****
        USER MAY  bound THE <print_symbol> to the instance, and
        this is why, iam accessing it via self
        so, it checks the object first, then the class if it's
        not in the obj.__dict__
        """
        rectangle = ""
        if not (self.width and self.height):
            return rectangle

        symbol = str(self.print_symbol)
        for _ in range(self.height - 1):
            rectangle += self.width * symbol
            rectangle += '\n'
        rectangle += self.width * symbol

        return rectangle

    def __repr__(self):
        """return the developer verstion of the object (A representation
        that can create a new object if passed to evel())"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return rect_2 if its area is bigger that rect_1
        and return rect_1 otherwise"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Return an object of Rectangle, with equal width and height
        aka, a square"""
        return cls(size, size)
