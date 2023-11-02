#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    args = argv[1:]
    summ = 0

    for arg in args:
        summ += int(arg)

    print(summ)
