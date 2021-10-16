#!/usr/bin/python3
"""Write to a text file"""


def write_file(filename="", text=""):
    """Writes a string to UTF"""
    with open(filename, "w") as fil:
        fil.write(text)
        return (len(text))
