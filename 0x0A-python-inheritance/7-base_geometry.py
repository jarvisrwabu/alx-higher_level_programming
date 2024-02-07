#!/usr/bin/python3
"""Inherited Class."""


class BaseGeometry:
    """Blueprint of superclass."""

    def area(self):
        """Area not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate input."""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
