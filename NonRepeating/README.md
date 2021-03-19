# Detecting first and all non-repeating characters

2021-03-22

#### About

The question came from an Amazon interview described in [YouTube video](https://www.youtube.com/watch?v=5co5Gvp_-S0).

#### Problem description

Find the first non-repeating characters in a given string. There are two variations in this question.

1. Non-sequential - Characters that appear sequentially on the spots are considered repeating. For example, the first non-repeating character in `aaabcccdeeb` is `b`. Although `b` appears twice, they do not sequentially appear.

2. Position independent - Characters that appear multiple times are considered repeating. For example, the first non-repeating character of `aaabcccdeeb` is `d` because it only appears once.

Find also all the non-repeating characters in a given string for the above two variations.

#### Example outputs

Type | `aaabcccdeeb` | `abcbad` | `abcabcabc`
-----|---------------|----------|------------
First/non-sequential | `b` | `a` | `a`
First/independent | `d` | `c` | None
All/non-sequential | `b, d, b` | `a, b, c, d` | `a, b, c`
All/independent | `d` | `c, d` | None
