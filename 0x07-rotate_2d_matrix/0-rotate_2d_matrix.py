#!/usr/bin/python3
"""A module that rotates a marix(2d)"""


def rotate_2d_matrix(matrix):
    """A func that rotates a matrix"""
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
