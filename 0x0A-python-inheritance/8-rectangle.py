#!/usr/bin/python3
"""Rectangle class"""


BaseGeometry = __import('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry class"""
    def __init__(self, width, height):
        """Validates height and width"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
