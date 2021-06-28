//
//  BinaryTree.hpp
//  
//
//  Created by Madhu RAJAGOPAL on 13/6/21.
//

#ifndef BinaryTree_hpp
#define BinaryTree_hpp

#include <iostream>

class BSTNode
{
public:
  BSTNode(int d)
   : data(d),
     left(nullptr),
     right(nullptr)
  {};
  ~BSTNode(){};
  int data;
  BSTNode *left;
  BSTNode *right;
};

class BST
{
public:
  BST();
  ~BST();
  int size(BSTNode *node);
  int height(BSTNode *node);
  BSTNode * insert(BSTNode *node, int d);
  void remove(BSTNode *node, int d);
  void erase(BSTNode *node);
  BSTNode * findMin(BSTNode *node);
  void levelOrderTraverse(BSTNode *node);
  void printCurrentLevel(BSTNode *node, int level);
  void traverseInOrder(BSTNode *node);
  void traversePreOrder(BSTNode *node);
  void traversePostOrder(BSTNode *node);
  BSTNode *root;
};

#endif /* BinaryTree_hpp */
