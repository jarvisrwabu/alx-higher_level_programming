#!/usr/bin/python3
def lookup(obj):
    """Return available class attributes and methods.

    Args:
        obj (object): Object to get attributes and methods.
    """
    return dir(obj)
