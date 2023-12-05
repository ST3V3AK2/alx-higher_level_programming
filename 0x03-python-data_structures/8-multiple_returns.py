#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if len(sentence) == 0:
        c = None
    else:
        c = sentence[0]
    return size, c
