#!/usr/bin/python3
""" Function to read a file """


def read_file(filename=""):
    """
    Reads a file and prints it

    Args:
        filename: the name of the file

    Return:
        None
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
