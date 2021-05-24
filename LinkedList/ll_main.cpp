#include "LinkedList.hpp"

/* Test */
int main()
{
  int a[] = {1,2,3,4,5,6,7,8,9,10};
  LinkedList l;
  for (int i = 0; i < 10; i++)
  {
    l.append(a[i]);
  }

  l.traverse();
  std::cout << "Size: " << l.size() << std::endl;

  l.remove(1);
  l.traverse();

  l.remove(2);
  l.traverse();

  l.remove(10);
  l.traverse();

  l.remove(5);
  l.traverse();
  std::cout << "Size: " << l.size() << std::endl;

  l.insertBefore(4,11);
  l.traverse();
  l.insertAfter(6,12);
  l.traverse();
  l.insertBefore(3,13);
  l.traverse();
  l.insertAfter(9,14);
  l.traverse();
  l.insertAfter(14,100);
  l.traverse();
  l.insertBefore(100,105);
  l.traverse();

  return 0;
}

