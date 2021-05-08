#!/usr/bin/env python
# 2021-05-02: Floyd's cycle detection algorithm

import sys

#       0   1   2   3   4   5   6   7   8   9   10  11  12  13  14
#                   *               *               *
arr1 = [10, 20, 30, 50, 60, 70, 80, 50, 60, 70, 80, 50, 60, 70, 80]
arr2 = [range(len(arr1))]

def floyd(arr):
    tortoise = 1
    hare = 2

    try:
        # Look for a(i) = a(2i)
        while arr[tortoise] != arr[hare]:
            tortoise += 1
            hare += 2
        print('Step 1: T {}, H {}'.format(tortoise, hare))

        # a(2i) - a(i) = kλ
        # Now look for the starting point μ
        hare = 0
        mu = 0
        while arr[tortoise] != arr[hare]:
            tortoise += 1
            hare += 1
            mu += 1
        print('Step 2: T {}, H {}, μ {}'.format(tortoise, hare, mu))

        # Find λ
        # Keep the tortoise still. Let hare advance.
        lamb = 1
        hare += 1
        while arr[tortoise] != arr[hare]:
            hare += 1
            lamb += 1
        print('Step 3: T {}, H {}, μ {}, λ {}'.format(tortoise, hare, mu, lamb))

    except IndexError:
        print('Reached the end. T {}, H {}'.format(tortoise, hare))
        print(sys.exc_info()[2].print_stack())
        return None

    return [mu, lamb]


if __name__ == '__main__':
    print(floyd(arr1))
    print(floyd(arr2))


