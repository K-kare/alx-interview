#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """Triangle"""
    if n <= 0:
        return []
    tri = [[1]]
    for row_num in range(1, n):
        row = [1]
        for j in range(1, row_num):
            element = tri[row_num - 1][j - 1] + tri[row_num - 1][j]
            row.append(element)
        row.append(1)
        tri.append(row)

    return tri
