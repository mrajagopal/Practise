#!/usr/bin/env python
# 2021-06-13: dictionary implementations

TREE = {
	'value': 15,
	'left': {
		'value': 10,
		'left': {
			'value': 8
		},
		'right': {
			'value': 12
		}
	},
	'right': {
		'value': 20,
		'left': {
			'value': 16
		},
		'right': {
			'value': 25
		}
	}
}

def traverse_tree(tree, level=0, accum=[]):
    accum.append((level, tree['value']))
    for left_right in ['left', 'right']:
        if left_right in tree:
            accum = traverse_tree(tree[left_right], level+1, accum)
    return accum

def print_tree(tree):
    accum = traverse_tree(tree, accum=[])
    for level, value in accum:
        print('{}{}'.format(level*' ', value))


print(TREE)
print(traverse_tree(TREE, accum=[]))
print_tree(TREE)