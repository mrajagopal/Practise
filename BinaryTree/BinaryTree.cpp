//
//  BinaryTree.cpp
//  
//
//  Created by Madhu RAJAGOPAL on 13/6/21.
//

#include "BinaryTree.hpp"

void debugLog(std::string &s, bool debug)
{
  if (debug)
    std::cout << s << std::endl;
}

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

BSTNode * BST::getParent(BSTNode *node, int d)
{
  BSTNode *parent = nullptr;
  while (node != nullptr && node->data != d)
  {
    parent = node;
    if (node->data > d)
      node = node->left;
    else
      node = node->right;
  }
  return parent;
}

void BST::remove(BSTNode *node, int d)
{
  BSTNode *parent = getParent(root, d);
  if (parent == nullptr)
  {
    std::cout << "Error: Item not found in tree" << std::endl;
    return;
  }
  else
  {
  }
  
  if (node == nullptr)
  {
    std::cout << "Error: Tree is empty" << std::endl;
    return;
  }
  
  
  // Traverse down the left of tree
  if (node->data > d)
  {
    remove(node->left, d);
  }
  // Traverse down the right of tree
  else if (node->data < d)
  {
    remove(node->right, d);
  }
  // At desired node to be deleted
  else
  {
    // Node to be deleted does not have a left subtree
    if ((node->left == nullptr) && (node->right != nullptr))
    {
      std::cout << "Node to be deleted does not have a left subtree" << std::endl;
      BSTNode *n = node->right;
      std::cout << node->data << " deleting" << std::endl;
      node->data = n->data;
      node->left = n->left;
      node->right = n->right;
      delete(n);
    }
    // Node to be deleted does not have a right subtree
    else if ((node->left != nullptr) && (node->right == nullptr))
    {
      std::cout << "Node to be deleted does not have a right subtree" << std::endl;
      BSTNode *n = node->left;
      node->data = n->data;
      node->left = n->left;
      node->right = n->right;
      delete(node->left);
    }
    // Node to be deleted is a leaf
    else if ((node->left == nullptr) && (node->right == nullptr))
    {
      std::cout << "Node to be deleted is a leaf" << std::endl;
      if (parent->left == node)
      {
        parent->left = nullptr;
        delete(node);
      }
      else
      {
        parent->right = nullptr;
        delete(node);
      }
    }
    // Node has both left and right subtrees
    else
    {
      BSTNode *successor = findMin(node->right);
      node->data = successor->data;
      remove(root, successor->data);
    }
  }
  return;
}

BSTNode * BST::insert(BSTNode *node, int d)
{
  if (node == nullptr)
  {
    std::cout << "New node: " << d << std::endl;
    node = new BSTNode(d);
    if (root == nullptr)
      root = node;
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

void BST::printBSTPreOrder(BSTNode *node)
{
  if (node == nullptr)
    return;
  
  std::cout << node->data << std::endl;
  printBSTPreOrder(node->left);
  printBSTPreOrder(node->right);
}

void BST::printBSTInOrder(BSTNode *node)
{
  if (node == nullptr)
    return;
  
  printBSTInOrder(node->left);
  std::cout << node->data << std::endl;
  printBSTInOrder(node->right);
}

void BST::printBSTPostOrder(BSTNode *node)
{
  if (node == nullptr)
    return;
  
  printBSTPostOrder(node->left);
  printBSTPostOrder(node->right);
  std::cout << node->data << std::endl;
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
//  std::cout << "Height of BST is " << h << std::endl;
  
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

BSTNode * BST::getRoot()
{
  return root;
}

bool BST::isBalanced(BSTNode *root)
{
  if (root == nullptr)
    return true;
  
  int lh = height(root->left);
  int rh = height(root->right);
  
  if (abs(lh - rh) > 1)
    return false;
  else if (!isBalanced(root->left) || !isBalanced(root->right))
    return false;
  
  return true;
}

bool BST::isValidBST(BSTNode *root)
{
  return isValidBSTVerify(nullptr, root, nullptr);
}

bool BST::isValidBSTVerify(BSTNode *lowerBound, BSTNode *node, BSTNode *upperBound)
{
  if (node == nullptr)
    return true;
  
  if (upperBound != nullptr && node->data >= upperBound->data)
    return false;
  
  if (lowerBound != nullptr && node->data <= lowerBound->data)
    return false;
  
  if (!isValidBSTVerify(lowerBound, node->left, node))
    return false;
  
  if (!isValidBSTVerify(node, node->right, upperBound))
    return false;
  
  return true;
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
  (void) b.insert(root, -5);
  (void) b.insert(root, 5);
  b.printBSTInOrder(root);
  std::cout << "The tree is " << (b.isBalanced(root) ? "balanced" : "unbalanced") << std::endl;
  (void) b.remove(root, -5);
  b.printBSTInOrder(root);
  (void) b.remove(root, 1000);
  b.printBSTInOrder(root);
  (void) b.remove(root, 400);
  b.printBSTInOrder(root);
  (void) b.remove(root, 5);
  b.printBSTInOrder(root);
  
  b.traverseInOrder(root);
  int h = b.height(root);
  std::cout << "Height of BST is " << h << std::endl;
  
  std::cout << std::endl;
  std::cout << "The size of the binary tree is " << b.size(root) << std::endl;
  b.levelOrderTraverse(root);
  
  std::cout << "The tree is " << (b.isBalanced(root) ? "balanced" : "unbalanced") << std::endl;
  std::cout << "The tree is " << (b.isValidBST(root) ? "a valid BST" : "not a valid BST") << std::endl;
  return 0;
}
