#!/usr/bin/python3
"""Base.py file"""


class Base:
    """Details for base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Integer id instantiation"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
