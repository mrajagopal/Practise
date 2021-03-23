# Radix sort

2021-03-29

#### About

Radix sort sorts a list of numbers by using the digit in a number as a sorting key and moving the key from the lowest to the highest (for descending). For example,

```
[53, 89, 150, 36, 633, 233]                                    # Original list
[150, 53, 633, 233, 36, 89]                                    # After sorted by the 1st (10^0) digit (0, 3, 3, 3, 6, 9)
[633, 233, 36, 150, 53, 89]                                    # After sorted by the 2nd (10^1) digit (3, 3, 3, 5, 5, 8)
[36, 53, 89, 150, 244, 633]                                    # After sorted by the 3rd (10^2) digit (0, 0, 0, 1, 2, 6)
```

Note:

- Do not change the order when the key is the same.
- Use 0 when there is no digit (e.g., 36's 3rd digit is 0).
- Can sort without comparison operators.

The complexity is O(wn), where w is the key length and n is the number of keys (e.g., n=10 and w=3 for three digits decimal numbers).

#### Problem statement

Sort a list of 5 three-digits numbers (0 to 999) using Radix sort. Do not use comparators.

#### References

- [Radix sort](https://en.wikipedia.org/wiki/Radix_sort), Wikipedia.
- [Radix Sort Algorithm Introduction in 5 Minutes](https://www.youtube.com/watch?v=XiuSW_mEn7g), YouTube.

