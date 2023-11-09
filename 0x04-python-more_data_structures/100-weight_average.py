#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)

    avg = 0
    size = 0
    for a, b in my_list:
        avg += a * b
        size += b
    return avg / size
