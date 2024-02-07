#!/usr/bin/python3
"""Class Rectangle that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Blueprint of Rectangle class inheriting BaseGeometry."""

    def __init__(self, width, height):
        """Initialize created objects."""
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
