#!/usr/bin/python3
def uppercase(str):
    temp = ""
    for char in str:
        c = ord(char)
        if c >= 97 and c <= 122:
            temp += chr(c - 32)
        else:
            temp += char
    print(temp)
