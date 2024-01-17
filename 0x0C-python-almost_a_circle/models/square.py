#!/usr/bin/python3
"""Simulate a square"""


from rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """instatiation of a Swquare instance"""
        super().__init__(size, size, x, y, id)
        self.size = size
    
    def __str__(self):
        """The string representation of the class"""
        msg = "[Square] ({}) {}/{} {}"
        return msg.format(self.id, self.x, self.y, self.size)
