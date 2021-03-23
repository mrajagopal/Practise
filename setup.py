#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'Practise',                                         # Package name
    version = '0.0.1',
    description = 'Excercising basic algorithms',
    author = 'Satoshi Toyosawa (Python) + Madhu Rajagopal (C++)',
    license = 'GPL',
    url = 'https://github.com/mrajagopal/Practise',
    packages = ['Utils']     # Will add these later ['BubbleSort', 'HeapSort', 'RadixSort', 'NonRepeating']
)