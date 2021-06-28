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

int BST::size(BSTNode *node)
{
  if (node == nullptr)
    return 0;
  
  return (size(node->left) + 1 + size(node->right));
}

BSTNode * BST::findMin(BSTNode *node)
{
  BSTNode *current = node;
  while (current && current->left != nullptr)
    current = current->left;
  
  return current;
}

void BST::traverseInOrder(BSTNode *node)
{
  if (node == nullptr)
  {
    return;
  }
  
  traverseInOrder(node->left);
  std::cout << node->data << " ";
  traverseInOrder(node->right);
}

void BST::traversePreOrder(BSTNode *node)
{
  if (node == nullptr)
  {
    return;
  }
  
  std::cout << node->data << " ";
  traversePreOrder(node->left);
  traversePreOrder(node->right);
}

void BST::traversePostOrder(BSTNode *node)
{
  if (node == nullptr)
    return;
  
  traversePostOrder(node->left);
  traversePostOrder(node->right);
  std::cout << node->data << " ";
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

int BST::height(BSTNode *node)
{
  while (node == nullptr)
    return 0;
  
  int lheight = height(node->left);
  int rheight = height(node->right);
  
  if (lheight > rheight)
    return (lheight + 1);
  else
    return (rheight + 1);
}

void BST::levelOrderTraverse(BSTNode *node)
{
  int h = height(node);
  std::cout << "Height of BST is " << h << std::endl;
  
  for (int i = 0; i <= h; i++)
    printCurrentLevel(node, i);
}

void BST::printCurrentLevel(BSTNode *node, int level)
{
  if (node == nullptr)
    return;
  
  if (level == 1)
  {
    std::cout << node->data << " ";
  }
  else if (level > 1)
  {
    printCurrentLevel(node->left, level - 1);
    printCurrentLevel(node->right, level - 1);
  }
}

int main()
{
//  int v[] = {1,2,3,4,5,6,7,8};
  BSTNode *root = nullptr;
  BST b;
  root = b.insert(root, 45);
  (void) b.insert(root, 25);
  (void) b.insert(root, 100);
  (void) b.insert(root, 1);
  (void) b.insert(root, 10);
  (void) b.insert(root, 200);
  (void) b.insert(root, 1000);
  (void) b.insert(root, 400);
  printBST(root);
  b.traverseInOrder(root);
  std::cout << std::endl;
  std::cout << "The size of the binary tree is " << b.size(root) << std::endl;
  b.levelOrderTraverse(root);
  return 0;
}
