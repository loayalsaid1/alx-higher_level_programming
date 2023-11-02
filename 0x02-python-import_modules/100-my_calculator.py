#!/usr/bin/python3
from sys import exit, argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    operations = {'+': add, '-': sub, '*': mul, '/': div}
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a, symbol, b = int(argv[1]), argv[2], int(argv[3])
        result = operations[symbol](a, b)
        print(f"{a} {symbol} {b} = {result}")
