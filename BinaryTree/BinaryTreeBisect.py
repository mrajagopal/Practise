#!/usr/bin/env python
# 2021-06-28: Binary Tree implementation - Using the Bisect library. Unfortunately, this does not show the tree itself.

import bisect

my_list = [15, 10, 8, 12, 20, 16, 25]
tree = []
for i in my_list:
    bisect.insort(tree, i)
print(tree)

# difference between _left and _right .... I don't see the difference
for i in my_list:
    left = bisect.bisect_left(tree, i)
    right = bisect.bisect_right(tree, i)                       # alias to bisect.bisect
    print('Finding {}. _left: {}, _right: {}'.format(i, left, right))

# Testing deletion
for i in my_list:
    left = bisect.bisect_left(tree, i)
    tree.remove(i)
    print('Removed {} at {}: {}'.format(i, left, tree))