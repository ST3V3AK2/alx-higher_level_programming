#!/usr/bin/python3
"""Creates a Rectangle class"""


class Rectangle:
    """Creates a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle arttributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the areas of two rectangle objects

        Args:
            rect_1: first rectangle object
            rect_2: second rectangle object

        Returns:
            The bigger rectangle or rect_1 if both are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2

    def area(self):
        """Calcuates the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Computes the perimeter of the rectangle"""
        perimeter = 0
        if self.__width > 0 and self.__height > 0:
            perimeter = self.__width * 2 + self.__height * 2
        return perimeter

    def __str__(self):
        """Prints a the square"""
        if self.__width == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                print(self.print_symbol, end="")
            if i < self.__height - 1:
                print("")
        return ""

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
