#!/usr/bin/python3

from functools import reduce


def roman_to_int(roman_string):
    """converts a Roman numeral to an integer."""

    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    res = 0

    while i < len(roman_string):
        if (i + 1 < len(roman_string) and
                roman[roman_string[i]] < roman[roman_string[i + 1]]):

            res += roman[roman_string[i + 1]] - roman[roman_string[i]]
            i += 2
        else:
            res += roman[roman_string[i]]
            i += 1

    return res
