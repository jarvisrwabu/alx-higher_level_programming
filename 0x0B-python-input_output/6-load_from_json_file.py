#!/usr/bin/python3
"""Creates Object from a JSON file."""


def load_from_json_file(filename):
    """Create Object from JSON file"""
    import json
    with open(filename, mode='r') as file:
        data = json.load(file)
