#!/usr/bin/python3
"""Return dictionary description."""


def class_to_json(obj):
    """Return dictionary description with simple data structure."""
    return obj.__dict__
