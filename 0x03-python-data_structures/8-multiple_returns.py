#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    char = sentence[0] if length else None

    return (length, char)
