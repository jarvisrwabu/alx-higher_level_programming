#!/usr/bin/python3
"""A function that checks if object is an instance of the class."""


def is_kind_of_class(obj, a_class):
    """Return true if obj is instance of a_class.

    Args:
        obj (object): Object to check.
        a_class (type): The class to verify object
    """
    return isinstance(obj, a_class)
