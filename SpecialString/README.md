# Special String Again

The problem is from Hacker Rank: [Prepare 》 Interview Preparation Kit 》 String Manipulation 》 Special String Again](https://www.hackerrank.com/challenges/special-palindrome-again).

## Problem

A string is said to be a special string if either of two conditions is met:

- All of the characters are the same, e.g. aaa.
- All characters except the middle one are the same, e.g. aadaa.

A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.

### Example

`s = mnonopoo`

`s` contains the following 12 special substrings:

`{m, n, o, n, o, p, o, o, non, ono, opo, oo}`

### Function Description

Complete the substrCount function in the editor below.

substrCount has the following parameter(s):

- int `n`: the length of string s
- string `s`: a string

### Returns

- int: the number of special substrings

### Input Format

The first line contains an integer, `n`, the length of `s`.

The second line contains the string `s`.

### Constraints

1 ≤ n ≤ 10<sup>6</sup>

Each character of the string is a lowercase English letter ascii[a-z],


## Samples

### Sample 0

#### Input 0

```
5
asasd
```

#### Output 0

```
7 
```

#### Explanation 0

The special palindromic substrings of `s = asasd` are `{a, s, a, s, d, asa, sas}`.

### Sample 1

#### Input 1

```
7
abcbaba
```

#### Output 1

```
10 
```

#### Explanation 1

The special palindromic substrings of `s = abcbaba` are `{a, b, c, b, a, b, a, bcb, bab, ada}`

### Sample 2

#### Input 2

```
4
aaaa
```

#### Output 2

```
10
```

#### Explanation 2

The special palindromic substrings of `s = aaaa` are `{a, a, a, a, aa, aa, aaa, aaa, aaaa}`.
