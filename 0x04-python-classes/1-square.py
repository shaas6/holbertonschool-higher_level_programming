#!/usr/bin/python3
# 1-square.py
"""Square class with size attribute"""


class Square:
    """Class defines square"""
    def __init__(self, size):
        """Sets size"""
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
