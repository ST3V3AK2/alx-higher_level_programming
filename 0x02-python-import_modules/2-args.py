#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ac = len(sys.argv) - 1
    message = "argument"
    if ac == 0:
        print("{} {}".format(ac, message + "s."))
        sys.exit()
    if ac > 1:
        message += "s"
    print("{} {}:".format(ac, message))
    for i in range(1, ac + 1):
        print("{}: {}".format(i, sys.argv[i]))
