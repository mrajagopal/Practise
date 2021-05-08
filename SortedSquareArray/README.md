# Sorted Square Array

#### About

I saw [this video](https://www.youtube.com/watch?v=4eWKHLSRHPY) and found it easy and fun. It appeared in a Facebook job interview. 

#### Problem description

- Let A be an array containing integer values -10000 ≤ A(i) ≤ 10000。
- A is sorted and not empty.
- Create a new sorted array from squares of A's elements.
- The algorithm must be efficient!

e.g., This does the job but slow (O is N + N log(N))

```
>>> A = [-10, -3, -1, 0, 2, 5]                           # Sorted
>>> B = [i*i for i in A]                                 # Create a square array (N)
>>> B
[100, 9, 1, 0, 4, 25]
>>> B.sort()                                             # Then sort (N logN)
>>> B
[0, 1, 4, 9, 25, 100]
```