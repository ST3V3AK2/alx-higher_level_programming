#!/usr/bin/python3
"""inherits_from function"""


def inherits_from(obj, a_class):
    """
    Checks if obj inherits from a_class indirectly or directly

    Args:
        obj: an instance of a class
        a_class: a class name

    Return:
        True if obj inherits directly or indirectly from a_class
    """
    return issubclass(obj.__class__, a_class) and type(obj) !=  a_class
