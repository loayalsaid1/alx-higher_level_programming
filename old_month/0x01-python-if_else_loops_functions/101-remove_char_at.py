#!/usr/bin/python3
def detect_outrange_index(str, n):
    if (n < 0) or (n >= len(str) and n != 0):
        return True


def remove_char_at(str, n):
    length = len(str)
    if detect_outrange_index(str, n):
        return (str)

    new_cpy = ""
    index = 0
    for index in range(n):
        new_cpy += str[index]

    if index == 0:
        index = 1
    else:
        index += 2
    for index in range(index, length):
        new_cpy += str[index]

    return (new_cpy)
