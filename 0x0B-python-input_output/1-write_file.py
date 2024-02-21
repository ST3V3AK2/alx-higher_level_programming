#!/usr/bin/python3
""" Creates a function that writes a string to a file """


def write_file(filename="", text=""):
    """
    Writes a string(text) to a file

    Args:
        filename: name of the file
        text: text to be written to file

    Return:
        Number of characters written to the file
    """
    with open(filename, "w", encoding = "utf-8") as file:
        return file.write(text)
