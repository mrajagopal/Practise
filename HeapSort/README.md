# Heap Sort

2021-03-22

#### About

(Max) Heap sort is

- A complete binary tree (a parent has one or two children)
- When the parent is the i-th element in an array, the children's locations are 2i+1 and 2i+2 respectively.
- All the parent node is greater than or equal to its childern, however, there is no relationship between the children.
- To **heapify** an array, recursively swap the three node values (parent and two children) to make the parent largest.
- To **heap sort** from a heapified array, recursively remove the root parent (guaranteed to be the largest) and heapify again.

(Min) Heap sort is a reverse of the max heap sort (the root is smallest).

The complexity (worst-case) is O(n log n).

#### Problem description

Implement the heap sort algorithm.

#### References

- [Heap Sort Algorithm](https://www.programiz.com/dsa/heap-sort), Programiz.