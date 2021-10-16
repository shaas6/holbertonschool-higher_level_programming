#!/usr/bin/python3
"""Append text to the end of a file"""


def append_write(filename="", text=""):
    """Appends string to end of a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
