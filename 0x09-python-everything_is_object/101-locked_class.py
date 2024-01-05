#!/usr/bin/python3
"""A locked class mudule"""


class LockedClass:
    """A locked class
    so you can't add any attibutes except first_name"""
    # def __setattr__(self, __name, __value):
    #     if __name != "first_name":
    #         raise AttributeError("'{}' object has no attribute {}".format(
    #             self.__class__.__name__, __name
    #         ))
    #     else:
    #         super().__setattr__(__name, __value)

    __slots__ = ["first_name"]
