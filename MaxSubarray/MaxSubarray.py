#!/usr/bin/env python
# 2021-05-04

import math


class MaxSubarray:

    def __init__(self, arr):
        self.N = len(arr)                                # The length of the original array
        self.start = -1                                  # The staring index of the maximum subarray
        self.length = -1                                 # The length of the subarray
        self.maximum = -math.inf                         # The maximum of this subarray
        self.array = arr

    def __str__(self):
        return 'S{}, L{}, M{}'.format(self.start, self.length, self.maximum)

    def getList(self):                                   # Show the list instead of start, length
        return self.array[self.start:self.start+self.length]


    def brute_force(self):
        '''
        O(N^2)
        Compare the current maximum and the subarray starting from the 'start' index and of length 'length'.
        if the subarray is larger, replace the properties.
        '''
        for length in range(1, self.N+1):
            for index in range(0, self.N-length+1):
                subarray = self.array[index:index+length]        # Subarray is a slice of the original array
                sigma = sum(subarray)
                if self.maximum < sigma:
                    self.start = index
                    self.length = length
                    self.maximum = sigma


    def kadane(self):
        '''
        local_max = 0
        global_max = -math.inf
        for i in range(0, self.N):
            local_max = max(self.array[i], self.array[i] + local_max)
            if local_max > global_max:
                global_max = local_max

        self.maximum = global_max
        '''

        local_max = 0
        self.maximum = -math.inf
        for index in range(0, self.N):
            flag = False
            if 
            local_max = max(self.array[index], self.array[index] + local_max)
            if local_max > self.maximum:
                self.maximum = local_max
                self.length += 1
                if local_max
            else:
                self.start = index
                self.length = 1


if __name__ == '__main__':
    test_list = {
        "test1": [-2, 1, -3, 4, -1, 2, 1, -5, 4],        # From Wikipedia
        "test2": [1, -3, 2, 1, -1],                      # https://www.youtube.com/watch?v=86CQq3pKSUw
        "test3": [-2, 1, -3, 4, -1, 2, 1, -5, 6, -1]     # ST
    }

    for name, arr in test_list.items():
        print('--- %s ---' % name)
        max_sub = MaxSubarray(arr)
        max_sub.brute_force()
        print(max_sub, max_sub.getList())
        max_sub.kadane()
        print(max_sub, max_sub.getList())
