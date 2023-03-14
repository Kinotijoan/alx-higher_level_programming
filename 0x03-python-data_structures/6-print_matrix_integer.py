#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for j in lst:
            print("{:d} ".format(j), end='')
        print()
