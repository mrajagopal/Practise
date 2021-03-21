#include <iostream>
#include <vector>

/*
void swap(int *a, int *b)
{
    int temp = a;
}
*/
void printVector(const std::vector<int>& v)
{
  for (int i = 0; i < v.size(); i++)
  {
    std::cout << v[i] << " ";
  }
  std::cout << std::endl;
}

void makeHeap(std::vector<int>& v, int n, int i) 
{ 
    int max = i; 
    int lhs = 2 * i + 1; 
    int rhs = 2 * i + 2;  
  
    // If left child is larger than root 
    if (lhs < n && v[lhs] > v[max]) 
        max = lhs; 
  
    // If right child is larger than largest so far 
    if (rhs < n && v[rhs] > v[max]) 
        max = rhs; 
  
    // If largest is not root 
    if (max != i) 
    { 
        std::swap(v[i], v[max]); 
  
        // Recursively heapify the affected sub-tree 
        makeHeap(v, n, max); 
    } 
}

void heapSort(std::vector<int>& v)
{
    int n = v.size();
    for (int i = n / 2 - 1; i >= 0; i--) 
        makeHeap(v, n, i); 
  
    // One by one extract an element from heap 
    for (int i = n - 1; i >= 0; i--) { 
        // Move current root to end 
        std::swap(v[0], v[i]); 
  
        // call max heapify on the reduced heap 
        makeHeap(v, i, 0); 
    } 
}

int main()
{
//  std::vector<int> v {14, 19, 9, 99, 100};
  std::vector<int> v {4, 10, 3, 5, 1};

  heapSort(v);
  printVector(v);
  return 0;
}
