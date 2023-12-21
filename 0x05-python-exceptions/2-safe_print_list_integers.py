#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            num = int(my_list[i])
        except (TypeError, ValueError):
            continue
        print("{:d}".format(num), end="")
        count += 1
    print("")
    return count
