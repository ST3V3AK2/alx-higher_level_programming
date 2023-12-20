#usr/bin/python3

class Square:
    """This creates a Square object and performs simple calculations
    on it"""
    def __init__(self, size=0)
        self.size = size
        try:
            temp = int(size)
            if temp < 0:
                raise ValueError
            self.size = temp
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            temp = int(size)
            if temp < 0:
                raise ValueError
            self.size = temp
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")


    def area(self):
        return size * size
