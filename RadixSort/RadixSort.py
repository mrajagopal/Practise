#!/usr/bin/env python
# 2021-03-22: Satoshi Toyosawa

import random
import math
import sys
import itertools

# Generate a list of N random numbers whose range is [0, max)
def random_array(N=10, max=1000):
    return [random.randrange(max) for num in range(N)]


# Extract the digit at the n-th position
def digit_at_nth(digit, n):
    pow = 10 ** n
    return math.floor(digit / pow) % 10


# Returns the list that are sorted based on the digit at the n-th position
def radix_sort_radix(arr, radix=0):
    tmp_array = []                                             # Create 10 empty bins.
    for i in range(10):                                        # The i-th element in the bin stores numbers that has i in the radix position.
        tmp_array.append([])

    for number in arr:
        dd = digit_at_nth(number, radix)                       # the digit at the radix-th position.
        tmp_array[dd].append(number)                           # Add it to dd-th array.

    return list(itertools.chain(*tmp_array))                   # flatten the array of arrays


# Radix sort
def radix_sort(arr):
    # Check the maximum length of the digits
    max_length = math.ceil(math.log10(max(arr)))               # Hmmm... 'max' may use comparison internally...

    for raidx in range(max_length):                            # Loop for the length of the longest number.
        new_array = radix_sort_radix(arr, raidx)
        arr = new_array

    return arr


if __name__ == "__main__":
    test_counts = 5

    print('Testing digit_at_nth ...')
    for i in range(test_counts):
        d = random.randrange(1000)
        pos = random.randrange(4)
        print('  %d at %d = %d' % (d, pos, digit_at_nth(d, pos)))

    print('Testing radix_sort_radix')
    for i in range(test_counts):
        rnd = random_array(5, 1000)
        pos = random.randrange(4)
        print('  %s at %d = %s' % (rnd, pos, radix_sort_radix(rnd, pos)))
    
    print('Testing radix_sort')
    for i in range(test_counts):
        rnd = random_array(10, 1000)
        print('  %s => %s' % (rnd, radix_sort(rnd)))

