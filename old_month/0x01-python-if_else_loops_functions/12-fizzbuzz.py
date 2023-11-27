#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0) or (i % 5 == 0):
            if (i % 3 == 0) and (i % 5 == 0):
                print("FizzBuzz", end=" ")
                continue
            elif (i % 3 == 0):
                print("Fizz", end=" ")
                continue
            else:
                print("Buzz", end=" ")
                continue
        else:
            print("{:d}".format(i), end=" ")
