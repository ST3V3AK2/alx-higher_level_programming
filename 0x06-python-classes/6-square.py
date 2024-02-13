#!/usr/bin/python3
"""Creates a Square Class"""


class Square:
    """This creates a Square object and performs simple calculations on it"""

    def __init__(self, size=0, position=(0, 0)):
        """The init method initializes classes private attributes"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Sets the current size of the square

        Args:
            size(int): the size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        return self.__size

    @property
    def position(self):
        """
        Sets the current position of the Square

        Args:
            position(int, int): the position of the square
        Raises:
            TypeError: if tuple does not contain 2 integers
        """
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif is_int(value[0]) is False or is_int(value[1]) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This calculates the area of the square

        Return:
            The area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints a the square
        """
        if self.__size == 0:
            print("")
            return

        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
