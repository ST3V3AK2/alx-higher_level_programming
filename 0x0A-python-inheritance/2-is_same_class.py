"""is_same_class function"""


def is_same_class(obj, a_class):
    """
    Checks if obj is an instance of a_class

    Args:
        obj: an instance of a class
        a_class: a class name

    Return:
        True if obj is an instance of a_class and False otherwise
    """
    return obj.__class__ is a_class
