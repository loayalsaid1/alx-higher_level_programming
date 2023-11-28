#!/usr/bin/python3
"""5-text_indentation module."""


def text_indentation(text):
    """print a text with no newline ending
    , and print 2 newlines after each '.', '?', ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not text:
        return

    line = ""
    for x in text:
        line += x
        if x in ('.', '?', ':'):
            print(f"{line.strip()}\n")
            line = ""
    if line:
        print(line.strip(), end='')
