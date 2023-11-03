#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator == "+":
        res = add(a, b)
    elif operator == "-":
        res = sub(a, b)
    elif operator == "*":
        res = mul(a, b)
    elif operator == "/":
        res = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, operator, b, res))
