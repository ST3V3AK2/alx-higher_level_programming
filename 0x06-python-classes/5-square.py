#!/usr/bin/python3

class Square:
    """This creates a Square object and performs simple calculations
    on it"""
    def __init__(self, size=0)
        self.size = size

    @property
    def size(self):
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
        return self.size * self.size

    def print(self):
        if self.size == 0
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print("")

