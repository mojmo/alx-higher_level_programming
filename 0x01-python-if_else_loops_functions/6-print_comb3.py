#!/usr/bin/python3

for n in range(0, 89):
    if n // 10 >= n % 10:
        continue
    print("{:02d}".format(n), end=", ")
else:
    print("{}".format(n + 1))
