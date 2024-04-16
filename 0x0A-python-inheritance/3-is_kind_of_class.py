#!/usr/bin/python3
"""is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or inherited from it

    Args:
        obj: a instance of a class
        a_class: a class name

    Return:
        True if obj is an instance or child of a_class else False
    """
    return isinstance(obj, a_class)
