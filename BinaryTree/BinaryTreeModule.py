#!/usr/bin/env python
# 2021-06-28: binaretree module (pip install binarytree)
#             See https://pypi.org/project/binarytree/

import binarytree as bt
from pprint import pprint

my_list = [15, 10, 8, 12, 20, 16, 25, 30]
my_tree = bt.build(my_list, is_balanced=False)
print(my_tree)
pprint(my_tree.properties)