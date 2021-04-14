#!/usr/bin/env python
# 2021-04-15: Sorted Square Array

# import math                                            # abs is not in math

def ssa(arr):
    ret = []

    neg_index = 0                                        # Read the negative values from left
    pos_index = len(arr) - 1                             # Read the positive values from right

    while neg_index <= pos_index:
        # Select the larger abs number
        if abs(arr[neg_index]) < abs(arr[pos_index]):
            target = arr[pos_index]
            pos_index -= 1
        else:
            target = arr[neg_index]
            neg_index += 1
        ret.append(target ** 2)

    ret.reverse()
    return ret


def ssa_orig(arr):

    ### The original algorithm first creates the return array of the same length
    ret = [i for i in range(len(arr))]

    neg_index = 0
    pos_index = len(arr) - 1
    ret_index = len(ret) - 1

    while neg_index <= pos_index:
        # select the larger number (same here)
        if abs(arr[neg_index]) < abs(arr[pos_index]):
            target = arr[pos_index]
            pos_index -= 1
        else:
            target = arr[neg_index]
            neg_index += 1

        # And fill the return array from the back!!
        ret[ret_index] = target ** 2
        ret_index -= 1

    return ret



if __name__ == '__main__':
    a = [-10, -3, -1, 0, 2, 5]
    print('Data: ', a)
    print('Mine: ', ssa(a))
    print('Orig: ',ssa_orig(a))