#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, length, x=0, y=0, id=None):
        """Rectangle initializer"""
        super().__init__(id)
        self.__width = Rectangle.check_attribute("width", width)
        self.__length = Rectangle.check_attribute("length", length)
        self.__x = Rectangle.check_attribute("x", x)
        self.__y = Rectangle.check_attribute("y", y)

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        self.__width = Rectangle.check_attribute("width", value)

    @property
    def length(self):
        """Length getter"""
        return self.__length

    @length.setter
    def length(self, value):
        """Length setter"""
        self.__length = Rectangle.check_attribute("length", value)

    @property
    def x(self):
        """X getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """X setter"""
        self.__x = Rectangle.check_attribute("x", value)

    @property
    def y(self):
        """Y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter"""
        self.__y = Rectangle.check_attribute("y", value)

    def area(self):
        """Calculate the area or a rectangle"""
        return self.width * self.length

    def display(self):
        """Print the rectangle"""
        print(self.y*'\n', end='')
        for x in range(self.length):
            print((self.x*' ')+'#'*self.width)

    def update(self, *args):
        """Update objet attributes as folows
            1st: id
            2nd: width
            3rd: length
            4th: x
            5th: y
        """
        try:
            self.id = args[0]
            self.width = args[1]
            self.length = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def __str__(self):
        """The str() output"""
        form = "[Rectangle] ({}) {}/{} - {}/{}"
        return form.format(self.id, self.x, self.y, self.width, self.length)

    @staticmethod
    def check_attribute(name, value):
        """Check if the value or the attirbute is valid.
            Otherwise, raise the correct Exception.
            Args:
                value: The object to be validated.
                name: the name of tha attirbute, used in exception message.

            Returns: The value back if it's valid.
        """
        def validate_type():
            """Validate if <value> is an int.

                Args:
                    value: The object to be validated.
                    name: the name of tha attirbute, used in exception message.
            """
            nonlocal name
            nonlocal value

            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")

        def validate_value():
            """Validate if <value> is > 0 or >= 0 if name is x or y
                Based on the name.

                Args:
                    value: The object to be validated.
                    name: the name of tha attirbute, used in exception message.
            """
            nonlocal name
            nonlocal value

            if name in ["width", "length"] and value < 1:
                raise ValueError(f"{name} must be > 0")
            elif name in ["x", "y"] and value < 0:
                raise ValueError(f"{name} must be >= 0")

        validate_type()
        validate_value()

        return value
