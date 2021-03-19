#!/usr/bin/env python
# 2021-03-15: Implementation of heap

# Definition.
# 1) A parent always have one or two children (binary tree)
# 2) Parent must be smaller than child (heap property)
# 3) Until all the elements in N-th level is filled, the next N+1 level is not created (shape property)
# 4) There is no magnitude relation in elements in the same child lavel.
#
# See also: https://medium.com/@yasufumy/data-structure-heap-ecfd0989e5be 

import random
import math
import heapq
import sys

def random_array(max=9):
    source = [i+1 for i in range(0, max)]
    random.shuffle(source)                                     # In-place
    return source


# Heapify the sub-tree from the index i.
# This operation guarantees that the i-th element is smallest in the tree (to the bottom)
# in-line replace
# 
def min_heapify(array, i, recurse=0):                          # i = parent's index number [0, N)
    indent = " " * recurse                                     # Shows recursion level.

    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i                                               # Assume the parent is the smallest

    print('%sChecking parent=%d, left=%d, right%d ... ' % (indent, i, left, right), end='')

    if left < len(array) and array[smallest] > array[left]:    # if left child is smaller than parent, left is smallerst
        smallest = left
    if right < len(array) and array[smallest] > array[right]:  # if right child is smaller than (parent or left), right is smallest.
        smallest  = right
    print('smallest=%d' % smallest)

    if smallest != i:                                          # There was a change. Swap.
        array[i], array[smallest] = array[smallest], array[i]
        recurse = recurse + 1
        min_heapify(array, smallest, recurse)


# Build the entire heap tree using min_heapify.
# We do not need to go down to the half of elements because they are checked by parents: i.e, Σ2**i = 2**(i+1) - 1)
# In-place replace
#
def min_heapify_build(array):
    for i in reversed(range(len(heaped1) // 2)):               # The last leaf nodes are not included (i.e, 
        min_heapify(heaped1, i)

# Heap-sort
# It is guaranteed that the first element is always the smallest in a heapified array
# while:
#  1) Swap array[0] and array[-1]    .... array[-1] is the smallest
#  2) Append array[-1] to a new sorted array.
#  3) Remove arrya[-1]
#  4) For the 0th index, run heapify.
#
def min_heap_sort(array):                                      # Assumed heapified.
    heaped = array.copy()
    sorted = []
    while len(heaped) > 0:
        heaped[0], heaped[-1] = heaped[-1], heaped[0]          # 1) Swap
        sorted.append(heaped[-1])                              # 2) Append
        del heaped[-1]                                         # 3) Remove
        min_heapify(heaped, 0)                                 # 4) Heapify 0th

    return sorted

# Heap add, remove and insert
# TBA


if __name__ == "__main__":
    try:
        max = int(sys.argv[1])
    except IndexError:
        max = 2**5 - 1

    source = random_array(max)
    print('Orig: %s' % source)

    heaped1 = source.copy()
    min_heapify_build(heaped1)
    print('heaped (by hand):   %s' % heaped1)

    heaped2 = source.copy()
    heapq.heapify(heaped2)
    print('heaped (by Python): %s' % heaped2)

    sorted = min_heap_sort(heaped1)
    print('sorted (by hand):   %s' % sorted)

