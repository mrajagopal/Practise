#include <iostream>
#include <utility>

void printArr(int v[], int size)
{
  for (int i = 0; i < size; i++)
  {
    if (i > 0 && i < size)
      std::cout << ",";

    std::cout << v[i];
  }
  std::cout << std::endl;
}

void bubble(int v[], int size)
{
  if (size == 1)
    return;
  for (int i = 0; i < size - 1; i++)
  {
    if (v[i] > v[i + 1])
    {
      std::swap(v[i], v[i + 1]);
    }    
  }
}

void bubbleSort(int v[], int size)
{
  for (int i = size; i > 1; i--)
  {
    bubble(v, i);
    std::cout << "loop #" << i << ":" << std::endl;
    printArr(v,i);
  }
}

int main()
{
  int v[] = {53, 89, 150, 36, 633, 233};

//  int v[] = {5,4,3,2,1};
  int size = sizeof(v)/sizeof(v[0]);
  std::cout << "Before:" << std::endl;
  printArr(v, size);

  bubbleSort(v, size);
  std::cout << "After:" << std::endl;
  printArr(v, size);
  return 0;
}
