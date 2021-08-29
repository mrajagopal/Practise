//
//  SkipList.hpp
//  
//
//  Created by Madhu RAJAGOPAL on 8/8/21.
//

#ifndef SkipList_hpp
#define SkipList_hpp

#include <cstdlib>
#include <cstring>

//#include
#define MAXLEVEL 5
class SkipNode
{
public:
  SkipNode(int &v, int l)
  : level(l)
  {
//    for (int i = 0; i < (level + 1); i++)
//      forwards[i] = nullptr;
    forwards = new SkipNode * [level + 1];
    memset(forwards, 0, sizeof(SkipNode*) * (level + 1));
    this->value = v;
  };
  
  ~SkipNode()
  {
    delete [] forwards;
  };
  
//private:
  int value;
  int level;
  SkipNode **forwards;
};

class SkipList
{
public:
  SkipList(int level);
  ~SkipList();
  void add(int val);
  
private:
  SkipNode *head;
  int level;
  int value;
};

#endif /* SkipList_hpp */
