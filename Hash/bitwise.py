#!/usr/bin/env python
# 2021-09-07: binaryarray and bitwise operations.
#             Just an exercise as np provides the functions

import sys

'''
Section 2, RFC 1321: 
- Each consecutive group of eight bits is interpreted as a byte with the high-order (most significant) bit of each byte listed first.
- Each consecutive group of four bytes is interpreted as a word with the low-order (least significant) byte given first.
'''

def bitwise_string(b_array):
    '''
    Convert the input binaryarray into binary and hex string
    '''
    if isinstance(b_array, bytearray) == False:
        print('This function is only for bytearray.')
        sys.exit(1)

    binary_string = ' '.join([format(b, '08b') for b in b_array])
    hex_string = ' '.join([format(b, '02x') for b in b_array])
    return binary_string + ', ' + hex_string


def bitwise_not(b_array):
    # & 0xFF is required as the NOT operation expects 32 bits signed integer
    return bytearray([(~b & 0xff) for b in b_array])


def bitwise_and(a_array, b_array):
    return bytearray([a & b for a, b in zip(a_array, b_array)])


def bitwise_or(a_array, b_array):
    return bytearray([a | b for a, b in zip(a_array, b_array)])


def bitwise_xor(a_array, b_array):
    return bytearray([a ^ b for a, b in zip(a_array, b_array)])


if __name__ == '__main__':
    word_A = bytearray([0x01, 0x23, 0x45, 0x67])
    word_B = bytearray([0x89, 0xab, 0xcd, 0xef])

    print('A:       ', bitwise_string(word_A))
    print('B:       ', bitwise_string(word_B))
    print('~A:      ', bitwise_string(bitwise_not(word_A)))
    print('~B:      ', bitwise_string(bitwise_not(word_B)))
    print('A & B:   ', bitwise_string(bitwise_and(word_A, word_B)))
    print('A | B:   ', bitwise_string(bitwise_or(word_A, word_B)))
    print('A xor B: ', bitwise_string(bitwise_xor(word_A, word_B)))
