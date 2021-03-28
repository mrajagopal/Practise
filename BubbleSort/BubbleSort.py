#!/usr/bin/env python
# Bubble sort
# 2021-03-23

import Utils                                                   # Satoshi's common functions

def bubble_sort(arr):
    length = len(arr)
    for j in range(length-1, 0, -1):                           # reverse order
        for i in range(0, j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

if __name__ == '__main__':
    for test in range(10):
        rand = Utils.random_array(10)
        arr = bubble_sort(rand)
        print('%s > %s' % (rand, arr))
