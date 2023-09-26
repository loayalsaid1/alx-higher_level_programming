#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    n = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end='')
            except (ValueError, TypeError):
                continue
            n += 1
    except IndexError:
        pass
    finally:
        print()

        return n
