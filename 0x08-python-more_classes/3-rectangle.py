#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """This is a Rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get Area of the Rectangle."""
        return (self.width * self.height)

    def perimeter(self):
        """Get Perimeter of the Rectangle."""
        if (self.width == 0) or (self.height == 0):
            return 0
        else:
            return (2*self.width) + (2*self.height)

    def __str__(self):
        """Get String Representation of Rectangle."""
        result = ""
        if (self.width == 0) or (self.height == 0):
            return result
        else:
            for i in range(self.height):
                for j in range(self.width):
                    result += "#"
            result += "\n"
        return result
