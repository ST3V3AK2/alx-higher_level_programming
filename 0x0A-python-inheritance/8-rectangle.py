#!/usr/bin/python3
"""Create a Rectangle Class"""


BaseGeometry = _import__('7-base-geometry').BaseGeometry


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
        super().__init__(self)
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
