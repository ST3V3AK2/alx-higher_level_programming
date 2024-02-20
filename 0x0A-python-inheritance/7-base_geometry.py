#!/usr/bin/python3
""" Creates a BaseGeometry class """

class BaseGeometry:
    """ Creates a BaseGeometry object """

    def __init__(self):
        """ Initalizes variables """
        pass

    def area(self):
        """ Calculates the area of the geometric shape """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates if value is an integer """
        if type(value) != int:
            raise TypeError("{name} must be an integer")
        elif value <= 0:
            raise ValueError("{name} must be greater than 0")
        else:
            return value
