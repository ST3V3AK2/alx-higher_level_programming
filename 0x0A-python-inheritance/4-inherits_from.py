#!/usr/bin/python
""" Class inheritance verification"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instancce of a class

    Args: 
        obj: object
        a_class: class

    Return:
        True if obj inherits from a_class else false
    """
    
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
