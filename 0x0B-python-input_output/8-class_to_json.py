#!/usr/bin/python3
""" Create a function that returns a dictionary description
of a object
"""


def class_to_json(obj):
    """
    Returns a dictionary description of an object

    Args:
        obj: input object

    Return:
        dictionary representation of object
    """
    return obj.__dict__
