#!/usr/bin/python3
"""A function to print a first an last name"""


def say_my_name(first_name, last_name=""):
    """A function to print a first and last name
    and of course, they must be strings"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is", end='')
    if first_name and last_name:
        print(f" {first_name} {last_name}")
    elif first_name:
        print(f" {first_name} ")
    else:
        print()
