#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    ac = len(sys.argv)
    for i in range(1, ac):
        result += int(sys.argv[i])
    print("{}".format(result))
