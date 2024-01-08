#!/usr/bin/python3
"""Make a rebel class of int
    by inverting it's equality functionality
"""


class MyInt(int):
    """MyInt class
        a subclass of int, overwrighting some functionlity
    """
    def __eq__(self, __value):
        """Invert the equality checking functionality
        """
        return super().__ne__(__value)

    def __ne__(self, __value):
        """Invert the un
        equality checking functionality
        """
        return super().__eq__(__value)
