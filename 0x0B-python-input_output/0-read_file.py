#!/usr/bin/python3
"""Function that reads a file."""


def read_file(filename=""):
    with open("filename", "r") as file:
        content = file.read()
        print(content)
