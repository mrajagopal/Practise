# Product of array except self

#### About

I saw [this video](https://www.youtube.com/watch?v=tSRFtR3pv74) and found it easy and fun. It appeared in an Apple job interview. 

#### Problem description

Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`. Do not use division!

Note: We are not after smaller O.

e.g., 

```
Input: [1, 2, 3, 4]
output: [24, 12, 8, 6]
```

The following code does the job, but it is NOT efficient and uses division.

```
>>> import functools
>>> a = [1, 2, 3, 4]                                     # input
>>> prod = functools.reduce(lambda x, y: x*y, a, 1)      # calculate product from all elements
>>> prod
24
>>> b = [prod/i for i in a]                              # divide by itself (No division!!)
>>> b
[24.0, 12.0, 8.0, 6.0]
```

