# Binary Tree

2021-06-15

#### About

A [binary tree](https://en.wikipedia.org/wiki/Binary_tree) is a data structure in which each node has the left and right children. The node can be represented as:

```
struct Node
{
    int data;
    Node *left, *right;
};
```

#### Problem description

![Binary tree sample](./BinaryTreeImage.png)

1. Represent the above tree in a code.
2. Write a routine to print 1.
3. Write a routine to insert a Node into the specified Node: e.g., insert(to_node, new_node).
4. Write a routine to delete a Node specified: e.g., delete(node).
5. There are different ways to traverse a tree: "inorder", "preorder" and "postorder". Implement them.

#### References

- [Top Algorithms/Data Structures/Concepts every computer science student should know](https://medium.com/techie-delight/top-algorithms-data-structures-concepts-every-computer-science-student-should-know-e0549c67b4ac), Techie Delight, 2018.
- [Tree Traversals (Inorder, Preorder and Postorder)](https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/), GeeksForGeeks, 2021.