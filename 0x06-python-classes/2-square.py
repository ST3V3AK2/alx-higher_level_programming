#!/usr/bin/python3
"""Create a Square Class"""


class Square:
    """This creates a Square object and performs simple calculations
    on it"""

    def __init__(self, size=0):
        """The init method initializes classes private attributes

        Args:
            size(int): the size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
