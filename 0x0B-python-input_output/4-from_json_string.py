#!/usr/bin/python3
"""Converts into python object"""
import json


def from_json_string(my_str):
    """Conversion string to obj"""
    return json.loads(my_str)
