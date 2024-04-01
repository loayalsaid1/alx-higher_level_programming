#!/usr/bin/python3
"""Find a peak of a list"""


def find_peak(ints):
    """Find the peak of a list"""
    if not ints:
        return None
    # found = False
    # length = len(ints)
    # if length == 1:
    #     return ints[0]
    # elif length == 2:
    #     return max(ints)
    # else:
    #     for idx in range(1, length-1):
    #         if ints[idx-1] <= ints[idx] >= ints[idx+1]:
    #             found = True
    #             break
    #     if found:
    #         return ints[idx]
    #     else:
    #         return max([ints[0], ints[-1]])

    try:
        if ints[0] > ints[1]:
            return ints[0]
        idx = 1
        while (True):
            if ints[idx-1] < ints[idx] > ints[idx+1]:
                return ints[idx]
            idx += 1
    except IndexError:
        return max(ints[0], ints[-1])
    else:
        return ints[0]
