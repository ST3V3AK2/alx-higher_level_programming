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

    def to_json(self):
        return self.__dict__
