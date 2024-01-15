#!/usr/bin/python3


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, length, x=0, y=0, id=None):
        """Rectangle initializer"""
        super().__init__(id)
        self.__width = width
        self.__length = length
        self.__x = x
        self.__y = y
    
    @property
    def width(self):
        """Width getter"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) is not float and type(value) is not float:
            raise TypeError("Width must be int or float.")
        if value < 0:
            raise ValueError("Width must be positive numebr.")
        self.__width = value

    @property
    def length(self):
        """Length getter"""
        return self.__length
    
    @length.setter
    def length(self, value):
        """Length setter"""
        if type(value) is not float and type(value) is not float:
            raise TypeError("Length must be int or float.")
        if value < 0:
            raise ValueError("Length must be positive numebr.")
        self.__length = value

    @property
    def x(self):
        """X getter"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """X setter"""
        if type(value) not in (int, float):
            raise TypeError("X must be int or float.")
        self.__x = value

    @property
    def y(self):
        """Y getter"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Y setter"""
        if type(value) not in (int, float):
            raise TypeError("Y must be int or float.")
        self.__y = value
