#include <iostream>

class Node
{
public:
  Node(int v): value(v), prev(nullptr), next(nullptr){};
  ~Node(){};

  int value;
  class Node *prev;
  class Node *next;
};

class DoublyLinkedList
{
public:
  DoublyLinkedList();
  ~DoublyLinkedList();
  int size();
  bool append(int v);
  bool remove(int v);
  void traverse();
  void rTraverse();
  
private:
  Node *head;
  Node *tail;
  int count;
};

DoublyLinkedList::DoublyLinkedList()
: count(0),
  head(nullptr),
  tail(nullptr)
{}

DoublyLinkedList::~DoublyLinkedList()
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

int DoublyLinkedList::size()
{
  return count;
}

bool DoublyLinkedList::append(int v)
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
    n->prev = tail;
    tail = n;
  }
  count++;
  return true;
}

void DoublyLinkedList::traverse()
{
  Node *n = head;
  while (n !=nullptr)
  {
    std::cout << n->value << " ";
    n = n->next;
  }
  std::cout << std::endl;
}

void DoublyLinkedList::rTraverse()
{
  Node *n = tail;
  while (n != nullptr)
  {
    std::cout << n->value << " ";
    n = n->prev;
  }
  std::cout << std::endl;
}

bool DoublyLinkedList::remove(int v)
{
  Node *n = head;
  if (head == nullptr)
    return false;
  
  while (n != nullptr)
  {
    if (n->value == v)
    {
      if ((head == n) && (tail == n))
      {
        head = nullptr;
        tail = nullptr;
        delete(n);
        count--;
        return true;
      }
      
      if (n == head)
      {
        head = n->next;
        head->prev = nullptr;
        delete(n);
        count--;
        return true;
      }
      else
      {
        n->prev->next =  n->next;
        delete(n);
        count--;
        return true;
      }
    }
    else
    {
      n = n->next;
    }
  }
  return false;
}

int main()
{
  int a[] = {1,2,3,4,5,6,7,8,9,10};
  DoublyLinkedList l;
  for (int i = 0; i < 10; i++)
  {
    l.append(a[i]);
  }

  l.traverse();
  std::cout << "Size: " << l.size() << std::endl;
  l.rTraverse();
  
  l.remove(1);
  l.traverse();
  
  l.remove(10);
  l.traverse();

  l.remove(5);
  l.traverse();

  return 0;
}
