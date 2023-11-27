#!/usr/bin/python3
capital = False
for i in range(25, -1, -1):
    if capital == 1:
        letter = i + 65
    else:
        letter = i + 97
    capital = not capital
    print("{:c}".format(letter), end="")
