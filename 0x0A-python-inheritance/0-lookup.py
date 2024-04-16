"""Lookup function"""


def lookup(obj):
    """
    Returns the list of attributes and methods in an object

    Args:
        obj: an object of a class

    Return:
        on success, list of available attributes and methods else empty list
    """
    return dir(obj)
