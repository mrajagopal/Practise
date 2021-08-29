//
//  SkipList.cpp
//  
//
//  Created by Madhu RAJAGOPAL on 8/8/21.
//

#include <cmath>
#include "SkipList.hpp"
#include "../LinkedList/LinkedList.hpp"

const float P = 0.5;
#define MAX_LEVEL 6

/*
 * Random Value Generator
 */
float frand()
{
    return (float) rand() / RAND_MAX;
}
 
/*
 * Random Level Generator
 */
int random_level()
{
    static bool first = true;
    if (first)
    {
        srand((unsigned)time(NULL));
        first = false;
    }
    int lvl = (int)(log(frand()) / log(1.-P));
    return lvl < MAX_LEVEL ? lvl : MAX_LEVEL;
}

SkipList::SkipList(int l)
: level(l), head(nullptr)
{
  head = new SkipNode (value,level);
}

SkipList::~SkipList()
{
  delete head;
}

void SkipList::add(int val)
{
  SkipNode *x = head;
  SkipNode *update[level + 1];
  memset(update, 0, sizeof(SkipNode*) * (level + 1));
  for (int i = level;i >= 0;i--)
  {
      while (x->forwards[i] != NULL && x->forwards[i]->value < value)
      {
          x = x->forwards[i];
      }
      update[i] = x;
  }
  x = x->forwards[0];
  if (x == NULL || x->value != value)
  {
      int lvl = random_level();
      if (lvl > level)
      {
          for (int i = level + 1;i <= lvl;i++)
          {
              update[i] = head;
          }
          level = lvl;
      }
      x = new SkipNode(lvl, value);
      for (int i = 0;i <= lvl;i++)
      {
          x->forwards[i] = update[i]->forwards[i];
          update[i]->forwards[i] = x;
      }
  }
}


int main ()
{
  int a[] = {1,2,3,4,5,6,7,8,9,10};
  LinkedList l;
  for (int i = 0; i < 10; i++)
  {
    std::cout << "Adding " << i << std::endl;
    l.append(a[i]);
  }
  SkipList sl(MAX_LEVEL);
//  (void)sl.add(5);
  return 0;
}
