#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index  in range(len(row)):
            if index == 0:
                print("{:d}".format(row[index]), end='')
            else:
                print(", {:d}".format(row[index]), end='')
        print("$")
