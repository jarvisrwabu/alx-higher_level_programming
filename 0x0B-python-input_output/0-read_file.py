#!/usr/bin/python3
"""Function that reads a file."""


def read_file(filename=""):
    """Read a file."""
    with open(filename, mode='r', encoding='UTF8') as file:
        content = file.read()
        print(content)
