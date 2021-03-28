#include <iostream>

void printArr(int v[], int size)
{
  for (int i = 0; i < size; i++)
  {
    if (i>0 && i < size)
      std::cout << ", " ;

    std::cout << v[i];
  }
  std::cout << std::endl;
}

void countSort(int v[], int size, int e)
{
  int output[size];
  int i, count[10] = { 0 };

  for (i = 0; i < size; i++)
  {
    count[(v[i] / e ) % 10]++;
  }

  for (i = 1; i < 10; i++)
  {
    count[i] += count[i - 1];
  }
  for (i = size - 1; i >= 0; i--)
  {
    output[count[(v[i] / e) % 10] - 1] = v[i];
    count[(v[i] / e) % 10]--;
  }

  for (i = 0; i < size; i++)
  {
    v[i] = output[i];
  }
    
}


int findMax(int v[], int size)
{
  int max = v[0];
  for (int i = 1; i < size; i++)
  {
    if (v[i] > max)
      max = v[i];
  }

  return max;
}


void radixSort(int v[], int size)
{
  int max = findMax(v, size);
  for (int e = 1; max/e > 0; e *= 10)
  {
    countSort(v, size, e);
  }
}

int main()
{
//  int data[] = {170, 45, 75, 90, 802, 24, 2, 66};
  int data[] = {53, 89, 150, 36, 633, 233};
  int size = sizeof(data)/sizeof(data[0]);
  printArr(data, size);

  radixSort(data, size);
  printArr(data, size);
  return 0;
}
