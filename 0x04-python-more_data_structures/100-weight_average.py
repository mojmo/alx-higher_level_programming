#!/usr/bin/python3

def weight_average(my_list=[]):
    """returns the weighted average of all integers
    tuple (<score>, <weight>)"""

    if len(my_list) == 0:
        return 0

    weight = 0
    score = 0

    for tup in my_list:
        score += tup[0] * tup[1]
        weight += tup[1]

    return score / weight
