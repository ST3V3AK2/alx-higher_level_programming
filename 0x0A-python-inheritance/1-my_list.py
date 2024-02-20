#!/usr/bin/python3
"""Create a list class"""


class MyList(list):
    """Create a list object"""

    def __init__(self):
        """ The init method intializes the inherited class attributes and methods"""
        super().__init__(self)

    def print_sorted(self):
        """ Prints the sorted(ascending) vertion of a list"""
        arr = self.copy()
        arr.sort()
        print(arr)
