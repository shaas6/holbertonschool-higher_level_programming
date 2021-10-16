#!/usr/bin/python3
"""Reads a file and prints to stdout"""


def read_file(filename=""):
    """Reads and prints the file"""
    with open(filename) as f:
        print(f.read(), end="")
