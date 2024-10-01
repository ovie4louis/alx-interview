#!/usr/bin/python3
"""
Pascals Triangle
"""


def pascal_triangle(n):
    """Getting the pascals triangle for n"""

    if n <= 0:
        return []

    PascalTriangle = []

    for row_number in range(n):
        row = [1] * (row_number + 1)

        for i in range(1, row_number):
            row[i] = (PascalTriangle[row_number-1][i-1] +
                      PascalTriangle[row_number-1][i])
        PascalTriangle.append(row)
    return PascalTriangle
