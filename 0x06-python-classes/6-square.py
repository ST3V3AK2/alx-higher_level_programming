#usr/bin/python3

class Square:
    """This creates a Square object and performs simple calculations
    on it"""
    def __init__(self, size=0, position=(0, 0))
        self.size = size
        self.position = position

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
            self.size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if (len(self.position != 2)):
                raise TypeError
            num_a = int(self.position[0])
            num_b = int(self.position[1])
        except TypeError:
            print("position must be a tuple of 2 positive integers")
        else:
            self.postion = value

    def area(self):
        return self.size * self.size

    def print(self):
        if self.size == 0
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print("")

    def position(self):

