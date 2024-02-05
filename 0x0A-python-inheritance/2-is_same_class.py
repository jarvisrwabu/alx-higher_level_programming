#!/usr/bin/python3
"""A function that checks if object is an exact instance of the class."""


def is_same_class(obj, a_class):
    """Return true if obj is instance of a_class.

    Args:
        obj (object): Object to check.
        a_class (type): The class to verify object
    """
    if a_class != object:
        if isinstance(obj, a_class):
            return True
        else:
            return False