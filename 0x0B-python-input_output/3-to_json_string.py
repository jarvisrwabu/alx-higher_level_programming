#!/usr/bin/python3
"""Function that converts to json_string."""


def to_json_string(my_obj):
    """Return JSON representation of Object."""
    import json
    content = json.dumps(my_obj)

    return content
