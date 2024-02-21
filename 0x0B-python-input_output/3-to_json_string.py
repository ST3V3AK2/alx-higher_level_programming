#!/usr/bin/python3
""" Creates a function that prints strings in JSON format """


import json


def to_json_string(my_obj):
    """
    Prints the JSON representation of an object

    Args:
         my_obj: input object

    Return:
        None
    """
    return json.dumps(my_obj)
