#!/usr/bin/python3
"""Function that writes to a file."""


def write_file(filename="", text=""):
    """Write to a file."""
    with open(filename, mode='w', encoding='UTF8') as file:
        content = file.write(text)

    return len(content)
