#!/usr/bin/python3

def is_same_class(obj, a_class):
    """ 
    Checks if obj is an instance of a_class

    Args:
        obj: created object
        a_class: test class

    Return:
        True if obj is an instance of a_class else False
    """
    if a_class == object:
        return False
    return isinstance(obj, a_class)
