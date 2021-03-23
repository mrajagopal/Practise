#!/usr/bin/env python
# 2021-03-23: Created random_array

import random

# Generate a list of random integers
#  N := A number of elements
#  max := Specified the range of random numbers: [0, max)
#  sequential := When True, generate numbers [max-N, max) sequentially and shuffle. e.g., max=11, N=10 generates [1, 2, ..., 10]
#
def random_array(N=10, max=1000, sequential=False):
    ret = []
    if sequential == True:
        ret = [i for i in range(max-N, max)]
        random.shuffle(ret)                                    # In-place    
    else:
        ret = [random.randrange(max) for num in range(N)]
    return ret


# Test routines
#
if __name__ == '__main__':
    print('random_array(10, 1000, False): ', random_array(10, 1000))
    print('random_array(10, 11, True): ', random_array(10, 11, True))