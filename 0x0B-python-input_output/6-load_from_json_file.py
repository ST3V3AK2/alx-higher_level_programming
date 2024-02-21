#!/usr/bin/python3
""" Create function that creates an object from a JSON File"""


import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file

    Args:
        filename: name of JSON file

    Return:
        Object created from JSON file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
