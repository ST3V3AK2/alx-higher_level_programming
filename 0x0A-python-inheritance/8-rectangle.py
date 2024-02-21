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
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
