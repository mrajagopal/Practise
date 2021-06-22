#!/usr/bin/env python
# 2021-06-13: Binary-search tree - dictionary implementation


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


### ----- Traversal methods ------

def traverse_preorder(tree, level=0, accum=[]):
	'''
	Depth-first, Pre-order
	Print the node upon first visit in the traversal.
	The output retains the structure of the tree (serialization).
	Example: 15 10 8 12 20 16 25
	'''
	accum.append((level, tree['value']))
	for left_right in ['left', 'right']:
		if left_right in tree:
			accum = traverse_preorder(tree[left_right], level+1, accum)
	return accum


def traverse_inorder(tree, level=0, accum=[]):
	'''
	Depth-first, In-order
	Print the node upon the second visit in the traversal.
	The output is sorderd (ascending).
	For decending order, visit right first (instead of left-first).
	Example: 8 10 12 15 16 20 25
	'''
	for left_right in ['left', 'right']:
		if left_right in tree:
			accum = traverse_inorder(tree[left_right], level+1, accum)
	accum.append((level, tree['value']))
	return accum


def traverse_postorder(tree, level=0, accum=[]):
	'''
	Depth-first, Post-order
	Print the node when it is last visisted in the traversal.
	The output shows the order of deletion from leafs to root.
	Example: 8 12 10 16 25 20 15
	'''
	for left_right in ['left', 'right']:
		if left_right in tree:
			accum = traverse_inorder(tree[left_right], level+1, accum)
		else:
			accum.append((level, tree['value']))
	return accum



def traverse_values(accum):
	'''
	Obtain the list of values from the list of accumulated node list (from the above traversal methods).
	'''
	return [node[1] for node in accum]


def print_tree(tree, level=0):
	''' preorder print '''
	print('{}{}'.format(level*' ', tree['value']))
	for left_right in ['left', 'right']:
		if left_right in tree:
			print_tree(tree[left_right], level+1)


def get_path_by_value(tree, value, path=[]):
	'''
	A search routine. Look for the value in the tree.
	Return the path to the node: e.g., ['left', 'left', 'value'].
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
	Auxiliary function to get the value from the tree path (see get_path_by_value).
	Return None if there is no such path (including an empty path)
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
	Insert a new leaf to the tree.
	If tree is None, there is no place to insert (in this implementation). Return 
	'tree' should not be empty (e.g., {}). 

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
	'''
	pass

print('--- Testing the traversal methods ---')
preorder = traverse_preorder(TREE)
print('1) Pre-order:   ', traverse_values(preorder))
inorder = traverse_inorder(TREE)
print('2) In-ordert:   ', traverse_values(inorder))
postorder = traverse_postorder(TREE)
print('3) Post-ordert: ', traverse_values(postorder))




'''
print('-- Testing get_path_by_value --')
for value in [8, 3, 1, 6, 4, 7, 10, 14, 13, 100]:
	path = get_path_by_value(TREE, value, path=[])	
	print('{} -> {} -> {}'.format(value, path, get_value_from_path(TREE, path)))
'''