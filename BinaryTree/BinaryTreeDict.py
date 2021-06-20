#!/usr/bin/env python
# 2021-06-13: Binary-search tree - dictionary implementation


TREE = {
	'value': 8,
	'left': {
		'value': 3,
		'left': {
			'value': 1
		},
		'right': {
			'value': 6,
			'left': {
				'value': 4,
			},
			'right': {
				'value': 7
			}
		}
	},
	'right': {
		'value': 10,
		'right': {
			'value': 14,
			'left': {
				'value': 13
			}
		}
	}
}

def traverse_tree(tree, level=0, accum=[], ):
    accum.append((level, tree['value']))
    for left_right in ['left', 'right']:
        if left_right in tree:
            accum = traverse_tree(tree[left_right], level+1, accum)
    return accum


def print_tree(tree, level=0):
	print('{}{}'.format(level*' ', tree['value']))
	for left_right in ['left', 'right']:
		if left_right in tree:
			print_tree(tree[left_right], level+1)


def get_path_by_value(tree, value, path=[]):
	'''
	A search routine. Look for the value in the tree.
	Return it's path to the node: e.g., ['left', 'left', 'value'].
	Return [] if no value is found.
	'''
	if tree['value'] == value:                                 # Found you.
		path.append('value')
		return path

	elif tree['value'] > value and 'left' in tree:             # node's value is larger than value AND there's a left key ==> GOTO left
		path.append('left')
		return get_path_by_value(tree['left'], value, path)

	elif tree['value'] < value and 'right' in tree:            # node's value is smaller than value AND there's a right key ==> GOTO right
		path.append('right')
		return get_path_by_value(tree['right'], value, path)

	return []                                                  # Not found


def get_value_from_path(obj, path):
	'''
	Auxiliary function for getting the value from the tree path (see get_path_by_value)
	'''
	if len(path) == 0:                                         # Empty path means no value found
		return None

	for subpath in path:
		try:
			obj = obj[subpath]
		except KeyError:
			return None

	# Check if it is not a dict object (not a lead node)
	if type(obj) == 'dict':
		return None

	return obj


def insert(tree, value):
	'''
	Insert a new leaf to the tree
	'''
	if not tree:                                               # Tree is empty. Create a new root node
		return {'value': value}

	elsif 


	if value < tree['value'] and 'left' in tree:             # node's value is larger than value AND there's a left key ==> GOTO left
		path.append('left')
		return get_path_by_value(tree['left'], value, path)


	elif tree['value'] < value and 'right' in tree:            # node's value is smaller than value AND there's a right key ==> GOTO right
		path.append('right')
		return get_path_by_value(tree['right'], value, path)

	return []            	


print('-- Testing print_tree --')
print_tree(TREE)

print('-- Testing get_path_by_value --')
for value in [8, 3, 1, 6, 4, 7, 10, 14, 13, 100]:
	path = get_path_by_value(TREE, value, path=[])	
	print('{} -> {} -> {}'.format(value, path, get_value_from_path(TREE, path)))
