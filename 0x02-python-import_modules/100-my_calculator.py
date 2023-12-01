#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    av = sys.argv
    ac = len(av) - 1
    if ac != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(av[1])
    b = int(av[3])
    if av[2] == "+":
        result = calc.add(a, b)
    elif av[2] == "-":
        result = calc.sub(a, b)
    elif av[2] == "*":
        result = calc.mul(a, b)
    elif av[2] == "/":
        result = calc.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, av[2], b, result))
