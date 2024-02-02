#!/usr/bin/python3
"""Function that adds 2 integers."""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int)(float): An integer or float
        b (int)(float): An integer or float
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a must be an integer or b must be an integer")

    elif isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
        return (a+b)

    else:
        return (a+b)
