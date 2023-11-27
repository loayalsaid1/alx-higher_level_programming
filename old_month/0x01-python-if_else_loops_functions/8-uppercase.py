#!/usr/bin/python3
def uppercase(str):
    for i in str:
        condition = (ord(i) >= 97) and (ord(i) <= 122)
        print("{:c}".format((ord(i) - 32) if condition else ord(i)), end="")
    print()
