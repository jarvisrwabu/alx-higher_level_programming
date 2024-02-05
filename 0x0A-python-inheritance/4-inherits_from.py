#!/usr/bin/python3
"""
Check if object is instance of the class that inherited from another class.
"""


def inherits_from(obj, a_class):
    """Definition for inherits checking.

    Args:
        obj (object): Object to check.
        a_class (type): The class to verify object
    """
    return isinstance(obj, type) and issubclass(type(obj), a_class)
