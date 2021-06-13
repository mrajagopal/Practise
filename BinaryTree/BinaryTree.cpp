//
//  BinaryTree.cpp
//  
//
//  Created by Madhu RAJAGOPAL on 13/6/21.
//

#include "BinaryTree.hpp"

BST::BST()
 : root(nullptr)
{}

BST::~BST()
{
  erase(root);
}

BSTNode * BST::findMin(BSTNode *node)
{
  BSTNode *current = node;
  while (current && current->left != nullptr)
    current = current->left;
  
  return current;
}

void BST::remove(BSTNode *node, int d)
{
  if (node == nullptr)
    return;
  
  if (node->data > d)
    remove(node->left, d);
  else if (node->data < d)
    remove(node->right, d);
  else
  {
    if (node->left == nullptr)
    {
      BSTNode *n = node->right;
      delete(node);
      return;
    }
    else if (node->right == nullptr)
    {
      BSTNode *n = node->left;
      delete node;
      return;
    }
    struct BSTNode* temp = findMin(node->right);
     
      // Copy the inorder
      // successor's content to this node
      node->data = temp->data;

      // Delete the inorder successor
      remove(node->right, temp->data);
  }
}

BSTNode * BST::insert(BSTNode *node, int d)
{
  if (node == nullptr)
  {
    std::cout << "New node: " << d << std::endl;
    node = new BSTNode(d);
  }
  else if (d > node->data)
  {
    node->right = insert(node->right, d);
  }
  else
  {
    node->left = insert(node->left, d);
  }
  return node;
}

void BST::erase(BSTNode *node)
{
  if (node == nullptr)
    return;

  erase(node->left);
  erase(node->right);
  delete node;
}

void printBST(BSTNode *node)
{
  if (node == nullptr)
    return;
  
  std::cout << node->data << std::endl;
  printBST(node->left);
  printBST(node->right);
}

int main()
{
//  int v[] = {1,2,3,4,5,6,7,8};
  BSTNode *root = nullptr;
  BST b;
  root = b.insert(root, 45);
  (void) b.insert(root, 25);
  printBST(root);
  
  return 0;
}
