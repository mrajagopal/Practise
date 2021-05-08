# Cycle detection

#### About

Cycle detection is the algorithmic problem of finding a cycle in a sequence of iterated function values (from [Wikipedia](https://en.wikipedia.org/wiki/Cycle_detection)).

```
[10, 20, 30, 50, 60, 70, 80, 50, 60, 70, 80, 50, 60, 70, 80, ...]
             ^               ^ Next cycle
             | Start of the cycle [50, 60, 70, 80]
```

There are several known algorithms:
- Floyd's tortoise and hare
- Brent's algorithm
- Gosper's algorithm

#### Problem statement

Obtain the starting element (e.g., 50 above) and frequency (e.g., 4) of the cycle using one or more cycle detection algorithms for a list of integers.

#### References

- [Cycle detection](https://en.wikipedia.org/wiki/Cycle_detection), Wikipedia.
