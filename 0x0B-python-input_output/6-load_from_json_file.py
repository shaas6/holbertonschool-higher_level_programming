#!/usr/bin/python3
"""Loads JSON"""
import json


def load_from_json_file(filename):
    """JSON to obj"""
    with open(filename, 'r') as fil:
        return json.loads(fil.read())
