#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum = 0
    for index in range(1, len(argv)):
        sum += int(argv[index])

    print(sum)
