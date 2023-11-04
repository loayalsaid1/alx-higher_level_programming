#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for row in matrix:
            last_index = len(row) - 1
            for i in range(last_index):
                print("{:d}".format(row[i]), end=' ')
            print("{:d}".format(row[last_index]))
    else:
        print()
