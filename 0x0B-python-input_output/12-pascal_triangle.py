#!/usr/bin/python3
"""Get n rows of pascals Triangle."""


def pascal_triangle(n):
    """Return n rows of pascals Triangle."""
    triangle = []
    for i in range(n):
        row = [0] * (i + 1)  # Initialize row with zeros
        row[0] = 1  # First element of each row is always 1
        row[-1] = 1  # Last element of each row is always 1
        if i >= 2:
            for j in range(1, i):  # Middle elements of the row
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle


# Recursive Approach -> Fails for large value of n
# """Get n rows of Pascal's Triangle."""


# def coefficient(n, k):
#     """Get Current coefficient using Recursion."""
#     if k == 0 or k == n:
#         return 1
#     return coefficient(n - 1, k) + coefficient(n - 1, k - 1)


# def pascal_triangle(n):
#     """Return n rows of Pascal's Triangle."""
#     if n <= 0:
#         return []
#     triangle = []
#     for i in range(n):
#         row = []
#         for j in range(i + 1):
#             row.append(coefficient(i, j))
#         triangle.append(row)
#     return triangle
