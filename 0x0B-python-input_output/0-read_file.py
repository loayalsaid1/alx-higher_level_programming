#!/usr/bin/python3
"""Read a file and print the content"""


def read_file(filename=""):
    """Read file <filename>

        Args:
            filename: The name of the file.

        Return: None
    """
    with open(filename) as f:
        print(f.read(), end="")
