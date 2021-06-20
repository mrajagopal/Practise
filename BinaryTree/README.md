# Binary Search Tree

2021-06-14

### About

A [binary search tree (BST)](https://en.wikipedia.org/wiki/Binary_search_tree) in this exercise is:

- A ordered (sorted) binary tree.
- A node has left and/or right children nodes or no child node (*leaf* node).
- Left child < Node < Right child

```
struct Node
{
    int data;
    Node *left, *right;
};
```

When the node does not have `*left` and `*right` children (e.g., `None` or `NULL`), it is called a *leaf*.

### Problem description

![Binary tree sample](./BinaryTreeImage.png)

1. Represent the above tree in a code.
2. Write a routine to print the tree.
3. Write a routine to insert a Node into the specified Node.
4. Write a routine to delete a Node.

In this exercise, pick a traversal method of your choice. There are:

- depth-first search (DFS)
    - inorder
    - preorder
    - postorder
- breadth-first search (BFS)

### References

- [Top Algorithms/Data Structures/Concepts every computer science student should know](https://medium.com/techie-delight/top-algorithms-data-structures-concepts-every-computer-science-student-should-know-e0549c67b4ac), Techie Delight, 2018.
- [Tree Traversals (Inorder, Preorder and Postorder)](https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/), GeeksForGeeks, 2021.