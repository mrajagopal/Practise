#!/usr/bin/env python
# 2021-03-08: Heaps, man. Using python's heapq module.
# 2021-03-21: Packaged random_array

import heapq
import random
import Utils

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
    rand = Utils.random_array(15, 15)
    print('Random:    %s' % rand)
    print('by Python: %s' % sort_by_python(rand))

