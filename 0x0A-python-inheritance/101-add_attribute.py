#!/usr/bin/python3
"""101-addAttribute Module

    Functions:
        add_attribute => Add attribute to an object if possible.
"""


def add_attribute(object, name, value):
    """Add_attribute
        Add attribute to an object if its class can hold new attributes.

        Args:
            object: The object itself.
            name: The name of the attr.
            value: The value of the attr.

        Return: None
    """
    if hasattr(object, '__dict__'):
        setattr(object, name, value)
        return
    else:
        raise TypeError("can't add new attribute")
