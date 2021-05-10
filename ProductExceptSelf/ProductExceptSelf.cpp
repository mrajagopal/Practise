//
//  ProductExceptSelf.cpp
//
//
//  Created by Madhu RAJAGOPAL on 8/5/21.
//

#include <iostream>
#define SIZE 4
void printArr(int v[], int size)
{
  for (int i = 0; i < size; i++)
  {
    std::cout << v[i] << " ";
  }
  std::cout << std::endl;
}

int main()
{
  int out[SIZE] = {1,1,1,1};
  int v[SIZE] = {1, 2, 3, 4};
  
  for (int i = 0; i < SIZE; i++)
  {
    for (int j = 0; j < SIZE; j++)
    {
      if (j != i)
        out[i] *= v[j];
    }
  }
  
  printArr(v, 4);
  printArr(out, 4);
  return 0;
}
