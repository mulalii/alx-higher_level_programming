#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            line = ''
            for col in row:
                line += "{:d} ".format(col)
            print(line[:-1])
