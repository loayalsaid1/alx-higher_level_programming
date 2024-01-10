#!/usr/bin/python3
"""Append to the end of a file and create it if it does exist"""


def append_write(filename="", text=""):
    """Append <text> the the end of <filename>
        and create it incase it doesn't exist.

        Args:
            filename: The name of the file.
            text: The text to insert.

        Return: The number of chars writen.
    """
    with open(filename, "a") as f:
        return f.write(text)
