#!/usr/bin/python3
"""Function that converts from json_string."""


def from_json_string(my_str):
    """Return Original from JSON."""
    import json
    content = json.loads(my_str)

    return content
