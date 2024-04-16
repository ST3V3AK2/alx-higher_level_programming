#!/usr/bin/python3
"""Create a Rectangle Class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates a Rectangle object"""

    def __init__(self, width, height):
        """
        Initializes input variables

        Args:
            width: width of the rectangle
            height: height of the rectangle

        Return:
            Nothing
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
