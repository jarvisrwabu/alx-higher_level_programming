#!/usr/bin/python3
"""Writes to text file using JSON Representation"""


def save_to_json_file(my_obj, filename):
    """Use JSON to write"""
    import json
    with open(filename, mode='w') as file:
        jstring = json.dumps(my_obj)
        file.write(jstring)
