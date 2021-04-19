#!/usr/bin/env python
# 2021-04-19: ST

import functools

# Time complexity O(2N)
def exceptSelf1(array):
    prod = functools.reduce(lambda x, y: x*y, array, 1)  # N
    ret = []
    for idx in array:                                    # N
        ret.append(int(prod/idx))
    return ret                                           # 2N

# Time complexity O(3N)
def exceptSelf2(array):
    length = len(array)
    forward = [None] * length
    backward = [None] * length
    result = [None] * length

    forward[0] = 1
    for i in range(0, length-1):                         # N
        forward[i+1] = forward[i] * array[i]

    backward[length-1] = 1                               # N
    for i in range(length-1, 0, -1):
        backward[i-1] = backward[i] * array[i]

    for i in range(length):                              # N
        result[i] = forward[i] * backward[i]

    return result                                        # 3N


# Less space required.
def exceptSelf3(array):
    length = len(array)
    result = [None] * length

    result[length-1] = 1                                 # First, create the backward
    for i in range(length-1, 0, -1):
        result[i-1] = result[i] * array[i]

    prod = 1
    for i in range(0, length-1):
        prod *= array[i]
        result[i+1] *= prod

    return result


if __name__ == '__main__':

    '''
    input = [1, 2, 3, 4]
    correct = [24, 12, 8, 6]
    '''

    input = [4, 5, 1, 8, 2]
    correct = [80, 64, 320, 40, 160]

    answer1 = exceptSelf1(input)
    print('Answer1: %s. %s' % ((correct == answer1), answer1))

    answer2 = exceptSelf2(input)
    print('Answer2: %s. %s' % ((correct == answer2), answer2))

    answer3 = exceptSelf3(input)
    print('Answer2: %s. %s' % ((correct == answer3), answer3))