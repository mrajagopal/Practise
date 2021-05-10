//
//  SortedSquareArray.cpp
//  
//
//  Created by Madhu RAJAGOPAL on 10/5/21.
//

#include <iostream>
#include <cmath>

#define SIZE 9

void printArr(int v[], int size)
{
  for (int i = 0; i < size; i++)
  {
    std::cout << v[i] << " ";
  }
  std::cout << std::endl;
}

void sortedSquaredArray(int v[], int size, int out[])
{
//  for (int i = 0; i < size; i++)
//  {
//    out[i] = v[i]*v[i];//^2;
//  }
  
  int nIndex = 0;
  int pIndex = SIZE-1;
  int pI = pIndex;
  int nI = nIndex;
  
  while (nIndex <= pIndex)
  {
//    std::cout << "nIndex: " << nIndex  << " " << "pIndex: " << pIndex << std::endl;
//    std::cout << "p[nIndex]: " << v[nIndex]  << " " << "v[pIndex]: " << v[pIndex] << std::endl;
//    std::cout << "nI: " << nI  << " " << "pI: " << pI << std::endl;

    if (std::abs(v[nIndex]) < std::abs(v[pIndex]))
    {
      out[pI] = v[pIndex]*v[pIndex];
      pIndex--;
      pI = pIndex;
      nI = nIndex;
    }
    else if (std::abs(v[nIndex]) == std::abs(v[pIndex]))
    {
      out[pI] = v[pIndex]*v[pIndex];
      out[pI-1] = v[pIndex]*v[pIndex];
      nIndex++;
      pIndex--;
      nI = nIndex;
      pI -= 2;
    }
    else
    {
      out[pI] = v[nIndex]*v[nIndex];
      nIndex++;
      nI = nIndex;
      pI = pIndex;

    }
//    printArr(out, size);
//    std::cout << "nI: " << nI  << " " << "pI: " << pI << std::endl;
  }
}

int main()
{
  int v[SIZE] = {-4,-3,-2,-1,1,2,3,4,5};
  int out[SIZE] = {0};
  sortedSquaredArray(v, SIZE, out);
  printArr(v, SIZE);
  printArr(out, SIZE);
  return 0;
}
