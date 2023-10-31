#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def get_last_digit(number):
    """get the last digit of a number"""
    if number > 0:
        return number % 10
    elif number == 0:
        return 0
    else:
        # Python divide differently
        return -1 * (10 - (number % 10))


last_digit = get_last_digit(number)
result = f"Last digit of {number} is {last_digit} and is "
if last_digit > 5:
    print(result + "greater than 5")
elif last_digit == 0:
    print(result + "0")
else:
    print(result + "less than 6 and not 0")
