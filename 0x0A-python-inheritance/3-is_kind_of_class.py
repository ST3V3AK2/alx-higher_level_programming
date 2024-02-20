#!/usr/bin/python3
""" Create a function verify inheritance"""

def is_kind_of_class(obj, a_class):
    """
    Checks if a object is an instance of a class or a subclass

    Args:
        obj: input object
        a_class: class

    Return:
        True if object is an instance of a_class else False
    """

    return isinstance(obj, a_class)
