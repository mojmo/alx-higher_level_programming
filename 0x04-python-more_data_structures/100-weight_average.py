#!/usr/bin/python3

def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple (<score>, <weight>)"""

    if len(my_list) == 0:
        return 0
    
    weight = 0
    score = 0

    for tup in my_list:
            score += tup[0] * tup[1]
            weight += tup[1]
    
    # avg = [[weight ** 2 for weight in tup] for tup in my_list]

    return score / weight

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))