#!/usr/bin/python3
"""Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Init the square and rectnanlge"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter in square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update objet attributes as follows
            1st: id
            2nd: size
            3rd: x
            4th: y

            if args exist and not empty, don't Consider kwargs
        """
        if args and len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
            return
        elif kwargs and len(kwargs) != 0:
            keys = ["id", "size", "x", "y"]
            for key in keys:
                if key in kwargs:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Return a dictionary or all attributes of an object"""
        id, s, x, y = self.id, self.size, self.x, self.y
        return {'id': id, 'size': s, 'x': x, 'y': y}

    def __str__(self):
        """Overwrite the __str__ function in Rectangle"""
        msg = "[Square] ({}) {}/{} - {}"
        return msg.format(self.id, self.x, self.y, self.size)
