#!/usr/bin/python3
"""Creates a Rectangle class"""

class Rectangle:
    """Creates a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle arttributes"""
        self.__width = width
        self.__height  = height

    @property
    def width(self):
        """
        Sets the current width of the rectangle

        Args:
            width(int): the width of the rectangle
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        return self.__width

    @property
    def height(self):
        """
        Sets the current height of the rectangle

        Args:
            width(int): the width of the erctangle
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
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
