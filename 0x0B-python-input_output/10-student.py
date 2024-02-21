#!/usr/bin/python3
""" Creates a Student class """


class Student:
    """ Creates a Student object """

    def __init__(self, first_name, last_name, age):
        """ initiaizes class variables

        Args:
            first_name: student's first name
            last_name: student's last name
            age: student's age

        Return:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictonary representatio of student

        Args:
            attrs: attribute names
        """
        new_dict = {}
        if attrs != None:
            for arg in self.__dict__.keys():
                if arg in attrs:
                    data = {arg: self.__dict__[arg]}
                    new_dict.update(data)
        else:
            new_dict = self.__dict__
        return new_dict
