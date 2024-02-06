#!/usr/bin/python3
"""Function that appends to a file."""


def append_write(filename="", text=""):
    """Append to a file."""
    with open(filename, mode='a', encoding='UTF8') as file:
        content = file.write(text)

    return content
