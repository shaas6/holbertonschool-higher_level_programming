#!/usr/bin/python3
"""Writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename=""):
    """converts obj to text with json"""
    with open(filename, 'w') as fil:
        fil.write(json.dumps(my_obj))
