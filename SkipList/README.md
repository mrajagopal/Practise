# Skip List

#### About

- A **skip list** is a linked list in layers, where the 'express lane' allows you to skip the nodes.
- A **skip list** is sorted.
- The complexity for insertion and deletion is `O(log n)`.
- The level (a number of lanes) is determined probabilistically (e.g., a chance of a node having three lanes is 0.125)

![Skip list example from Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Skip_list.svg/500px-Skip_list.svg.png)

#### Problem statement

- Implement a node object/structure.
- Implement a search (by value) function.
- Implement a insertion function.
- Implement a delete function.


#### References

- [Wikipedia Skip List](https://en.wikipedia.org/wiki/Skip_list).
- [SkipList documentation for C++/Python APIs by Paul Ross](https://skiplist.readthedocs.io/en/latest/). See [Github](https://github.com/paulross/skiplist) for the source.
- [A simple SkipList implementation in python by Sachin Nair](https://gist.github.com/sachinnair90/3bee2ef7dd3ff0dc5aec44ec40e2d127).
- [Skip List video by Idiomatic Programmers](https://www.youtube.com/watch?v=rhKuVZSsU_Q), 5:49.

