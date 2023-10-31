#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    results = []

    for i in range(list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except TypeError:
            print("wrong type")
            quotient = 0
        finally:
            results.append(quotient)
    return results