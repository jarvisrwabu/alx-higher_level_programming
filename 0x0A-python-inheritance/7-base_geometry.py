#!/usr/bin/python3
"""Create a new BaseClass."""


class BaseGeometry:
    """BaseClass to be inherited."""

    def __init__(self, name, value):
        """Initialize an object."""
        self.name = name
        self.value = value

    def integer_validator(self, name, value):
        """Validate integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))

        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))

    def area(self):
        """Area not implemented."""
        raise Exception("area() is not implemented")
