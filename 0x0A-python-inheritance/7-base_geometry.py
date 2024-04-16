#!/usr/bin/python3
""" Create BaseGeometry Class"""


class BaseGeometry:
    """Cretaes a BaseGeometry object"""

    def __init__(self):
        """Initializes class variables"""
        pass

    def area(self):
        """Calculates the area of BaseGeometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

        Args:
            name: name of value
            value: value

        Return:
            value
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            return value
