#!/usr/bin/python3
""" My function """

def pascal_triangle(n):
    """ 
    Generates nxn pascal's triangle

    Args:
        n: size of the pascals triangle

    Return:
        pascals triangle
    """

    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        temp = []
        if i == 0:
            temp.append(1)
            triangle.append(temp)
            continue
        else:
            for idx, num in enumerate(triangle[i - 1]):
                if idx == 0:
                    temp.append(1)
                    continue
                val = triangle[i - 1][idx - 1] + num
                temp.append(val)
            temp.append(1)
            triangle.append(temp)
    return triangle
