#!/usr/bin/python
# Find the nont repeating elements
# From https://www.youtube.com/watch?v=5co5Gvp_-S0
# 2021-03-15

from collections import OrderedDict

### Interpretation 1: The order matters
## Return: {pos: char, ...}
#
def orderMatter(ss, all=True):
    arr = list(ss)
    arr.insert(0, None)
    arr.append(None)

    ret = {}
    for i in range(1, len(arr)-1):
        if arr[i-1] != arr[i] and arr[i] != arr[i+1]:
            # Return once I found the first one.
            if all == False:
                return {i-1: arr[i]}                           # Deduct 1 because I added None.
            # Otherwise accumulate.
            ret[i-1] = arr[i]

    return ret

### Interpretation 2: The order does not matter
## 
def orderNoMatter(ss, all=True):
    # Create a dict {char: counts, ...}
    dic = {}
    for c in ss:
        dic[c] = dic.setdefault(c, 0) + 1

    # A list of characters that appear only once.
    arr = [key for (key, val) in dic.items() if val == 1]

    # Check if the character in arr is found
    ret = {}
    for i in range(len(ss)):
        if ss[i] in arr:
            if all == False:
                return {i: ss[i]}
            ret[i] = ss[i]

    return ret


# ans:  b              c         None
strs = ['aaabcccdeef', 'abcbad', 'abcabcabc']

for ss in strs:
    print('----' + ss)
    for tf in [True, False]:
        s = str(tf)[0]
        print('Order matter    (all=%s): %s' % (s, orderMatter(ss, all=tf)))
        print('Order no matter (all=%s): %s' % (s, orderNoMatter(ss, all=tf)))
