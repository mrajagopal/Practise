//
//  CycleDetection.cpp
//  
//
//  Created by Madhu RAJAGOPAL on 11/5/21.
//

// 1. Initialize two pointers (tortoise and hare) that both point to the head of the linked list
// 2. Loop as long as the hare does not reach null
// 3. Set tortoise to next node
// 4. Set hare to next, next node
// 5. If they are at the same node, reset the tortoise back to the head.
// 6. Have both tortoise and hare both move one node at a time until they meet again
// 7. Return the node in which they meet
// 8. Else, if the hare reaches null, then return null

#include "../LinkedList/LinkedList.hpp"

Node* detectCycle(Node *head)
{
  Node *tortoise = head;
  Node *hare = head;
  
  if (head == nullptr)
    return nullptr;

  while (hare->next != nullptr && hare->next->next != nullptr)
  {
    std::cout << "tortoise: " << tortoise->value << " hare: " << hare->value << std::endl;
    tortoise = tortoise->next;
    hare = hare->next->next;
    
    if (tortoise->value == hare->value)
    {
      std::cout << "match: " << tortoise->value << std::endl;
      tortoise = head;
      while (tortoise->value != hare->value)
      {
        tortoise = tortoise->next;
        hare = hare->next;
      }
      return (hare);
    }
  }
  
  return nullptr;
}

int main()
{
  int v[] = {10, 20, 30, 50, 60, 70, 80, 50, 60, 70, 80, 50, 60, 70, 80};
  int size = sizeof(v)/sizeof(v[0]);
  LinkedList l;

  for (int i = 0; i < size; i++)
  {
    l.append(v[i]);
  }
  l.traverse();
  if (detectCycle(l.getHead()))
  {
    std::cout << "Cycle found" << std::endl;
  }
  else
  {
    std::cout << "No cycle found" << std::endl;
  }

  return 0;
}

