#!/usr/bin/env python
# 2021-03-08 - Heaps, man. Using python's heapq module.

import heapq;
import random;

### Generate a list of 'max' elements with random numbers in [0, max)Random array for test
def random_array(max=15):
    return [random.randrange(max) for num in range(max)]      

### Heap-sort using Python's heappop and append
# Actually, heapify itself does not sort the elements.
# "Heap" in Python merely means h[k] < h[2k+1] && h[k] < h[2k+2].
def sort_by_python(data):
    heaped = data.copy()
    heapq.heapify(heaped)                                      # in-place
    heap_sorted = []
    for i in range(len(heaped)):
        min = heapq.heappop(heaped)                            # heappop picks up the smallest element from the heap.
        heap_sorted.append(min)
    return heap_sorted


if __name__ == '__main__':
    rand = random_array()
    print('Random:    %s' % rand)
    print('by Python: %s' % sort_by_python(rand))

