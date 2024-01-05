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
        self.size = size

    @property
    def size(self):
        """
        Sets the current size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        try:
            self.size = int(self.size)
            if self.size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        else:
            self.__size = valu


    def area(self):
        """This calculates the area of the square"""
        return self.size * self.size

    def print(self):
        """Prints a the square"""
        if self.size == 0
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print("")

