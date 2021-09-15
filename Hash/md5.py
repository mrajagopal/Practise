#!/usr/bin/env python
# 2021-08-30

import hashlib
import sys


def md5_padding(data):                                         # Input: bytes
    '''
    Procedure in 3.1 and 3.2 in RFC 1321.

    The raw data must be padded to make the length multiple of 64 bytes (512 bytes).
    The first byte is 1000.0000 (0x80).
    The next bytes are 0000.0000 (0x00).
    The last 8 bytes (64 bits) are the length (in little endian: See section 3.3)
    '''

    # Convert bytes to bytearray
    raw_bytes = bytearray(data)
    print('Padding: Raw data (bytes): {}/{}'.format(len(raw_bytes), hex(len(raw_bytes))))

    # Length is the lower 8 bytes of the original length
    length = (len(raw_bytes) & 0xFFFFFFFFFFFFFFFF).to_bytes(8, 'little')
    print('Padding: Length in 8-bytes format: {}'.format(length.hex('-')))

    # The input must be multiple of 64 bytes, including the leading 0x80 and the 8 bytes length
    zero_paddings = 64 - len(raw_bytes) % 64 - 1 - 8
    if zero_paddings < 0:
        zero_paddings += 64
    print('Padding: A number of zero bytes: {}'.format(zero_paddings))

    # Create the padded bytes
    padded_bytes = raw_bytes + bytearray(b'\x80') + bytearray(zero_paddings) + length

    # Check if I got this correct
    print('Padding: Total padded length (bytes): {}'.format(len(padded_bytes)))
    if len(padded_bytes) % 64 != 0:
        print('Padding: I got the padding wrong!!')
        sys.exit()

    return(padded_bytes)                                       # Return padded bytearray



def md5(data):                                                 # Input: bytes
    # Section 3.3
    word_A = bytearray([0x01, 0x23, 0x45, 0x67])
    word_B = bytearray([0x89, 0xab, 0xcd, 0xef])
    word_C = bytearray([0xfe, 0xdc, 0xba, 0x98])
    word_D = bytearray([0x76, 0x54, 0x32, 0x10])
    print_words(word_A)

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        filename = sys.argv[0]                                 # This file.

    with open(filename, 'br') as f:                            # binary mode.
        data = f.read()
    f.close()
    print('{} bytes read from {}.'.format(len(data), filename))

    print('--- Testing built-in md5')
    m = hashlib.md5()
    m.update(data)
    md5lib = m.digest()                                        # Returns bytes
    print('Digest size: {} bits, Block size: {} bits, Digest (hex): {}'.format(m.digest_size*8, m.block_size*8, md5lib.hex()))

    print('--- Testing padding function')
    md5_padding(b'satoshi')
    md5_padding(bytes(range(60)))

    print('--- Testing bitwise-word operations')
    test_word = bytearray([0x01, 0x23, 0x45, 0x67])
    print('Word-Op: Not: {}'.format(word_not(test_word)))
    # rint('\n'.join(print_words()))

