#!/usr/bin/python3
"""Creates a Rectangle Class"""


class Rectangle:
    """Creates a Rectangle"""

    def __init__(self, width=0, height=0):
        """ Intializes the input variables """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Sets the width of the rectangle

        Args:
            width(int):  the width of the rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if the width is less than 0
        """
        return self.__width

    @property
    def height(self):
        """
        Sets the height of the rectangle

        Args:
            height(int): the height of the rectangle

        Raises:
            TypeError: if the height is not an integer
            ValueError: if the height is less than 0
        """
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Computes the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Computes the perimeter of the Rectangle"""
        perimeter = 0
        if self.__width > 0 and self.__height > 0:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter
