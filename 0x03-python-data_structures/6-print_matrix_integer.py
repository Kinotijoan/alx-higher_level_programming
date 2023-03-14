#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
<<<<<<< HEAD
    for lst in matrix:
        for j in lst:
            print("{:d} ".format(j), end='')
        print()
=======
    '''print a matrix of integers'''

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j != (len(matrix[i]) - 1):
                print(" ", end="")
        print("")
>>>>>>> 8b0b14f75ac72c18d737d93b69dcb40c633b532e
