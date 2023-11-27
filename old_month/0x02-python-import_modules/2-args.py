#!/usr/bin/python3
from sys import argv as args

if __name__ == "__main__":
    args_len = len(args) - 1
    if args_len == 0:
        print("0 arguments.")
    elif args_len == 1:
        print("1 argument:")
        print("1: {}".format(args[1]))
    else:
        print(str(args_len) + " arguments:")
        for index in range(1, args_len + 1):
            print("{}: {}".format(index, args[index]))
