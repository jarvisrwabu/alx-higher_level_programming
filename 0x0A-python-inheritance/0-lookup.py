#!/usr/bin/python3
"""A function that Returns available class attributes and methods."""


def lookup(obj):
    """Return available class attributes and methods.

    Args:
        obj (object): Object to get attributes and methods.
    """
    return dir(obj)
