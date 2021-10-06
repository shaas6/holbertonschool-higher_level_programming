#!/usr/bin/python3
# 2-square.py
""" Square class for size and errors """


class Square:
    """ Size definition """
    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    """ Area definition """
    def area(self, size=0):
        calc_area = self.__size ** 2
        return calc_area
