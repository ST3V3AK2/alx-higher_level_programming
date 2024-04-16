#!/usr/bin/python3
"""Creates a Square Class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates a Square object"""

    def __init__(self, size):
        """ Initializes class variables """
        self.integer_validator("size", size)

        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """ Print a representation of Square"""
         return f"[Square] {self.__size}/{self.__size}"
