#!/usr/bin/env python
# 2021-08-30

import hashlib
import sys

def md5(bytes):
    pass


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        filename = sys.argv[0]                                 # This file.

    with open(filename, 'br') as f:                            # binary mode.
        data = f.read()
    f.close()
    print('{} bytes read from {}.'.format(len(data), filename))

    m = hashlib.md5()
    m.update(data)
    md5lib = m.digest()                                        # Returns bytes
    print('Digest size: {} bits, Block size: {} bits, Digest (hex): {}'.format(m.digest_size*8, m.block_size*8, md5lib.hex()))