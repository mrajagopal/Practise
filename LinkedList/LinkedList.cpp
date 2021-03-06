//#include <iostream>
//
//class Node
//{
//public:
//  int value;
//  class Node *next;
//  Node(int v) : value(v), next(nullptr) {};
//};
//
//class LinkedList
//{
//public:
//  LinkedList();
//  ~LinkedList();
//  int size();
//  void append(int v);
//  bool remove(int v);
//  void traverse();
//  bool insertBefore(int b, int v);
//  bool insertAfter(int a, int v);
//  int getTail();
//
//private:
//  Node *head;
//  Node *tail;
//  int count;
//};

#include "LinkedList.hpp"

LinkedList::LinkedList()
: head(nullptr),
  tail(nullptr),
  count(0)
{}

LinkedList::~LinkedList()
{
  Node *n = head;
  while (n != nullptr)
  {
    Node *next = n->next;
    delete(n);
    n = next;
    count--;
  }
}

int LinkedList::size()
{
  return LinkedList::count;
}

void LinkedList::append(int v)
{
  Node *n = new Node(v);
  if (head == nullptr)
  {
    head = n;
    tail = head;
  }
  else
  {
    tail->next = n;
    tail = n;
  }
  count++;
}

bool LinkedList::remove(int v)
{
  Node *n = head;
  Node *prev = nullptr;
  
  if (head == nullptr)
    return false;
  
  while(n != nullptr)
  {
    std::cout << "Node: " << n->value << std::endl;
    if (n->value == v)
    {
      if ((n == head) && (n == tail))
      {
        std::cout << "Head & Tail" << std::endl;
        delete(n);
        head = nullptr;
        tail = nullptr;
        count--;
        return true;
      }
      
      if (n == head)
      {
        std::cout << "Head Only" << std::endl;
        head = n->next;
        prev = n;
        delete(n);
        count--;
        return true;
      }
      else
      {
        std::cout << "Middle" << std::endl;
        prev->next = n->next;
        delete(n);
        count--;
        return true;
      }
    }
    else
    {
      prev = n;
      n = n->next;
    }
  }
  return false;
}

void LinkedList::traverse()
{
  Node *n = head;
  while (n != nullptr)
  {
    std::cout << n->value << " ";
    n = n->next;
  }
  std::cout << std::endl;
}

bool LinkedList::insertBefore(int b, int v)
{
  Node *n = head;
  Node *prev = nullptr;
  while (n != nullptr)
  {
    if (n->value == b)
    {
      Node *newNode = new Node(v);
      newNode->next = n;
      if (prev)
        prev->next = newNode;
      else
        head = newNode;
      
      return true;
    }
    
    prev = n;
    n = n->next;
  }
  return false;
}

bool LinkedList::insertAfter(int a, int v)
{
  Node *n = head;
  Node *prev = nullptr;
  while (n != nullptr)
  {
    if (n->value == a)
    {
      Node *newNode = new Node(v);
      newNode->next = n->next;
      n->next = newNode;
      if (prev)
        prev->next = n;
      
      if (newNode->next == nullptr)
        tail = newNode;
      
      return true;
    }
    prev = n;
    n = n->next;
  }
  return false;
}

Node * LinkedList::getHead()
{
  return head;
}

int LinkedList::getTail()
{
  return tail->value;
}

/* Test */
//int main()
//{
//  int a[] = {1,2,3,4,5,6,7,8,9,10};
//  LinkedList l;
//  for (int i = 0; i < 10; i++)
//  {
//    l.append(a[i]);
//  }
//
//  l.traverse();
//  std::cout << "Size: " << l.size() << std::endl;
//
//  l.remove(1);
//  l.traverse();
//
//  l.remove(2);
//  l.traverse();
//
//  l.remove(10);
//  l.traverse();
//
//  l.remove(5);
//  l.traverse();
//  std::cout << "Size: " << l.size() << std::endl;
//
//  l.insertBefore(4,11);
//  l.traverse();
//  l.insertAfter(6,12);
//  l.traverse();
//  l.insertBefore(3,13);
//  l.traverse();
//  l.insertAfter(9,14);
//  l.traverse();
//  l.insertAfter(14,100);
//  l.traverse();
//  l.insertBefore(100,105);
//  l.traverse();
//
//  return 0;
//}

