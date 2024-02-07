#!/usr/bin/python3
"""Get dictionary description within a class."""


class Student:
    """Blueprint of student."""

    def __init__(self, first_name, last_name, age):
        """When initializing new object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get dictionary representation of student instance."""
        return self.__dict__
