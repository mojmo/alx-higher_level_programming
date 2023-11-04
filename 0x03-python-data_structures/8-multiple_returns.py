#!/usr/bin/python3

def multiple_returns(sentence):
    """returns a tuple with the length of a string and its first character."""

    new_tuple = len(sentence), sentence[0]

    if sentence == '':
        new_tuple = (len(sentence), None)

    return new_tuple
