#include <iostream>

class Node
{
public:
  Node(int v) : value(v){};
  ~Node(){};
  int value;
  class Node *next;
};

class CircularLinkedList
{
public:
  CircularLinkedList();
  ~CircularLinkedList();
  bool append(int v);
  bool traverse();
  bool remove(int v);
  bool insertBefore(int b, int v);
  bool insertAfter(int a, int v);
  int size();
  
private:
  Node *head;
  Node *tail;
  int count;
};

CircularLinkedList::CircularLinkedList()
: head(nullptr),
  tail(nullptr),
  count(0)
{}

CircularLinkedList::~CircularLinkedList()
{
  Node *n = head;
  if (head == nullptr)
  {
    return;
  }
  else
  {
    tail->next = nullptr;
  }
  
  while (n != nullptr)
  {
    Node *next = n->next;
    delete(n);
    n = next;
  }
}

int CircularLinkedList::size()
{
  return count;
}

bool CircularLinkedList::append(int v)
{
  Node *n = new Node(v);
  if (head == nullptr)
  {
    count++;
    head = n;
    tail = n;
    tail->next = head;
    return true;
  }
  
  count++;
  tail->next = n;
  tail = n;
  tail->next = head;
  return true;
}

bool CircularLinkedList::traverse()
{
  Node *n = head;
  while (n != nullptr)
  {
    std::cout << n->value << " ";
    if (n == tail)
      break;
    
    n = n->next;
  }
  std::cout << std::endl;
  return true;
}

bool CircularLinkedList::insertBefore(int b, int v)
{
  Node *n = head;
  Node *prev = nullptr;
  while (n != nullptr)// && tail->next != head)
  {
    if (n->value == b)
    {
      Node *newNode = new Node(v);
      newNode->next = n;
      if (prev)
      {
        prev->next = newNode;
      }
      else // We are inserting before the head
      {
        tail->next = newNode;
        head = newNode;
      }
      return true;
    }
    prev = n;
    n = n->next;
  }
  return false;
}

bool CircularLinkedList::insertAfter(int a, int v)
{
  Node *n = head;
  while (n != nullptr)
  {
    if (n->value == a)
    {
      Node *newNode = new Node(v);
      newNode->next = n->next;
      n->next = newNode;
      if (n == tail)
      {
        tail = newNode;
      }
      return true;
    }
    n = n->next;
  }
  return false;
}

bool CircularLinkedList::remove(int v)
{
  Node *n = head;
  Node *prev = nullptr;
  
  if (n == nullptr)
    return false;
  
  while (n != nullptr)
  {
    if (n->value == v)
    {
      if ((n == head) && (n == tail))
      {
        head = nullptr;
        tail = nullptr;
        count--;
        delete(n);
        return true;
      }
      else if (n == head)
      {
        head = n->next;
        tail->next = head;
        delete(n);
        count--;
        return true;
      }
      else if(n == tail)
      {
        tail = prev;
        tail->next = head;
        delete(n);
        count--;
        return true;
      }
      else
      {
        prev->next = n->next;
        delete(n);
        count--;
        return true;
      }
    }
    else
    {
      if (n == tail)
        break;
      
      prev = n;
      n = n->next;
    }
  }
  return false;
}

int main()
{
  int a[] = {1,2,3,4,5,6,7,8,9,10};
  CircularLinkedList c;
  
  for (int i = 0; i < 10; i++)
  {
    c.append(a[i]);
  }

  c.traverse();
  c.remove(5);
  c.traverse();
  c.remove(1);
  c.traverse();
  c.remove(10);
  c.traverse();
  c.remove(10);
  c.traverse();
  c.remove(3);
  c.traverse();
  c.remove(2);
  c.traverse();
  c.insertAfter(9,1);
  c.traverse();
  c.insertBefore(9,10);
  c.traverse();
  c.insertBefore(4,100);
  c.traverse();
  c.insertBefore(100,110);
  c.traverse();
  c.insertAfter(100,105);
  c.traverse();

  return 0;
}
