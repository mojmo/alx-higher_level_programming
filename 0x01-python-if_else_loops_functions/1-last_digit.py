#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 > 5:
    last_digit = 'and is greater than 5'
elif number % 10 == 0:
    last_digit = 'and is 0'
elif number % 10 < 6 and not 0:
    last_digit = 'and is less than 6 and not 0'
print(f"Last digit of {number} is {number % 10}", last_digit)
