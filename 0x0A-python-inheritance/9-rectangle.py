#!/usr/bin/python3
""" Creates a rectagle class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Creates a rectangle object """

    def __init__(self, width, height):
        """ 
        Initializes the variables 

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

    def area(self):
        """ Computes the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Prints an acceptable represntation of the parameters """
        return f"[Rectangle] {self.__width}/{self.__height}"
