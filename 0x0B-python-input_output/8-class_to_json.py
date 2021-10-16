#!/usr/bin/python3
"""Object to JSON"""


def class_to_json(obj):
    """Returns dictionary description of obj"""
    return obj.__dict__
