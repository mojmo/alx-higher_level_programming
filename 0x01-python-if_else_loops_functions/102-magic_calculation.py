#!/usr/bin/python3

def magic_calculation(a, b, c):
    """Execute a magical computation"""
    if a < b:
        return c
    elif c > b:
        return a + b

    return a * b - c
