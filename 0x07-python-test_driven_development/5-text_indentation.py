#!/usr/bin/python3
"""Adds two new lines after . ? :"""


def text_indentation(text):
    """Replaces certain input with newlines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    newtext = text.replace('?', '?\n\n')
    newtext = text.replace('.', '.\n\n')
    newtext = text.replace(':', ':\n\n')
    print("\n".join([item.strip() for item in newtext.split("\n")]), end="")
