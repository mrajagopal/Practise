//
//  LinkedList.hpp
//  
//
//  Created by Madhu RAJAGOPAL on 16/5/21.
//

#ifndef LinkedList_h
#define LinkedList_h

#include <iostream>

class Node
{
public:
  int value;
  class Node *next;
  Node(int v) : value(v), next(nullptr) {};
};

class LinkedList
{
public:
  LinkedList();
  ~LinkedList();
  int size();
  void append(int v);
  bool remove(int v);
  void traverse();
  bool insertBefore(int b, int v);
  bool insertAfter(int a, int v);
  int getTail();

private:
  Node *head;
  Node *tail;
  int count;
};

#endif /* LinkedList_h */
