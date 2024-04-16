#!/usr/bin/python3
"""Create a Rectangle Class"""


BaseGeometry = _import__('7-base_geometry').BaseGeometry


def Rectangle(BaseGeometry):
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
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)


    def area(self):
        """ Computes the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Prints an acceptable represntation of the parameters """
        return f"[Rectangle] {self.__width}/{self.__height}"
