#!/usr/bin/python3
# Recursive Approach
"""Get n rows f Pascal's Triangle."""


def coefficient(n, k):
    """Get Current coefficient using Recursion."""
    if k == 0 or k == n:
        return 1
    return coefficient(n - 1, k) + coefficient(n - 1, k - 1)


def pascal(n):
    """Return n rows of Pascal's Triangle."""
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(coefficient(i, j))
        triangle.append(row)
    return triangle
