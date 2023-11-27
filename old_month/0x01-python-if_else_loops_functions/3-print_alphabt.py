#!/usr/bin/python3
for index in range(97, 123):
    if index == 101 or index == 113:
        continue
    print("{0:c}".format(index), end="")
