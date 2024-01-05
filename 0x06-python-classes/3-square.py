#!/usr/bin/python3
"""Creates a Square Class"""


class Square:
    """This creates a Square object and performs simple calculations
    on it"""


    def __init__(self, size=0)
        """The init method initializes classes private attributes

        Args:
            size(int): the size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        try:
            temp = int(size)
            if temp < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        else:
            self.__size = temp

    def area(self):
        """This calculates the area of the square"""
        return self.__size * self.__size
