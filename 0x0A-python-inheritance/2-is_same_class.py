#!/usr/bin/python3
""" Create a functon to identify a class """


def is_same_class(obj, a_class):
    """ 
    Checks if obj is an instance of a_class

    Args:
        obj: created object
        a_class: test class

    Return:
        True if obj is an instance of a_class else False
    """
    return obj.__class__ is a_class
