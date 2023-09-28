#!/usr/bin/python3
from sys import argv as args

if __name__ == "__main__":
    sum = 0
    for index in range(1, len(args)):
        sum += int(args[index])

    print(sum)
