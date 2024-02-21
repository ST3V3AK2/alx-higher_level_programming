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
        if attrs != None:
            new_dict = {arg: self.__dict__[arg] for arg in self.__dict__.keys() & attrs}
        else:
            new_dict = self.__dict__
        return new_dict

    def reload_from_json(self, json):
        """
        Replaces all the attributes of Student

        Args:
            json: a dictionary of updated attributes
        """
        for key in json:
            self.__dict__[key] = json[key]
