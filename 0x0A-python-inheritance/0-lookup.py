#!/usr/bin/python3
""" Lookup Fuunction """


def lookup(obj):
    """
    Returns a list of available attributes and methods in an object 

    Args:
        obj: the object

    Return:
        list of avaiable attributes
    """
    return dir(obj)
