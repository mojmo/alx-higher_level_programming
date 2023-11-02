#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    args = argv[1:]
    args_len = len(argv) - 1

    if (args_len == 0):
        print("0 arguments.")
    else:
        print("{} argument{}:".format(args_len, 's' if args_len > 1 else ''))

        for arg in range(1, args_len + 1):
            print("{}: {}".format(arg, argv[arg]))
