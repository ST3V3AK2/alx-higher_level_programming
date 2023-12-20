#usr/bin/python3

class Square:
    """This creates a Square object and performs simple calculations
    on it"""
    def __init__(self, size=0):
        try:
            temp = int(size)
            if self.size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

    def area(self):
        return size * size
