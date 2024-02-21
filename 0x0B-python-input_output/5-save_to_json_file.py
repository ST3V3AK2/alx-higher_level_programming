#!/usr/bin/python3
""" Creates a function that saves data to a json file """


import json


def save_to_json_file(my_obj, filename):
    """
    Saves data to a json file

    Args:
        my_obj: input data
        filename: name of json file

    Return:
        None
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
