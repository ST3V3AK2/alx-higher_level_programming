#!/usr/bin/python3
def no_c(my_string):
    size = len(my_string)
    for i in range(size):
        if my_string[i].lower() in "cC":
            my_string[i] = ""
    return my_string
