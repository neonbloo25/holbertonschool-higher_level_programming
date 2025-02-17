#!/usr/bin/python3
"""I/O Week! YAY TRIANGLES!!!"""


def pascal_triangle(n):
    """Target Function"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        previous_row = triangle[i - 1]
        new_row = [1]

        for j in range(len(previous_row) - 1):
            new_row.append(
                previous_row[j] + previous_row[j + 1]
            )

        new_row.append(1)
        triangle.append(new_row)

    return triangle
