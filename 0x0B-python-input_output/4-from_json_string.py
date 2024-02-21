#!/usr/bin/python3
""" Creates a function to decodes a JSON string"""


import json


def from_json_string(my_str):
    """
    Converts from JSON forma to an object

    Args:
        my_str: JSON string

    Return:
        None
    """
    return json.loads(my_str)
