#!/usr/bin/python3
""" Creates a function that appends strings to files """


def append_write(filename="", text=""):
    """
    Appends a string(text) to a file

    Args:
        filename: name of the file
        text: string to be appended to file

    Return:
        number of characters appended to file
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
