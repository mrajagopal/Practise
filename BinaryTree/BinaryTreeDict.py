#!/usr/bin/env python
# 2021-06-13: Binary-search tree - dictionary implementation
#
# See also (in Japanese)
# - https://www.delftstack.com/ja/howto/python/python-tree/ ... Insertion and in-order traversal
# - https://engineeringnote.hateblo.jp/entry/python/algorithm-and-data-structures/binary_tree ... The codes for pre/in/post are easy to understand.
# - https://qiita.com/maebaru/items/a47c2ef675a76e8816ab ... Deletion

import json
from queue import Queue                                        # First in, First out


def traverse_preorder(tree):
	'''
	Depth-first, Pre-order.
	Print the node upon first visit in the traversal.
	The output retains the structure of the tree (serialization).
	Example: 15 10 8 12 20 16 25

	Implemented using closure.
	'''
	accum = []

	def _inner(tree, level=0):                                 # _ before function means "weak internal use". from X import * does not load these functions.
		accum.append((level, tree['value']))                   # Add the node when it was first visited.
		for left_right in ['left', 'right']:
			if left_right in tree:
				_inner(tree[left_right], level+1)

	_inner(tree)
	return accum


def traverse_inorder(tree, level, accum):
	'''
	Depth-first, In-order
	Print the node upon the second visit in the traversal.
	The output is sorderd (ascending).
	For decending order, visit right first (instead of left-first).
	Example: 8 10 12 15 16 20 25

	Implemented in the usual recurseion.
	Hence the 'accum' object is reused (the same ID) if you do not explictly specify in the argument, don't write 'accum=[]' in the argument.
	'''
	if 'left' in tree:
		accum = traverse_inorder(tree['left'], level+1, accum)

	accum.append((level, tree['value']))                       # Add the node when the search for one child completes.

	if 'right' in tree:
		accum = traverse_inorder(tree['right'], level+1, accum)

	return accum


def traverse_postorder(tree, level, accum):
	'''
	Depth-first, Post-order
	Print the node when it is last visisted in the traversal.
	The output shows the order of deletion from leafs to root.
	Example: 8 12 10 16 25 20 15
	'''
	for left_right in ['left', 'right']:
		if left_right in tree:
			accum = traverse_postorder(tree[left_right], level+1, accum)
	accum.append((level, tree['value']))                       # Add the node when the search for both children complete.

	return accum

def traverse_breadth_first(tree):
	'''
	Breadth-first (BFS)
	'''
	queue = Queue()                                            # Create an empty queue
	queue.put((0, tree))                                       # Add the root tree to the queue in level 0.
	accum = []                                                 # Keep (level, subtree)
	while not queue.empty():
		l, subtree = queue.get()
		accum.append((l, subtree['value']))
		for left_right in ['left', 'right']:
			if left_right in subtree:
				queue.put((l+1, subtree[left_right]))          # Add the left/right subtrees at the level one below.

	return accum


def traverse_values(accum, indent=False):
	'''
	Obtain the list of values from the list of accumulated node list (from the above traversal methods).
	To indent by the 'level', set indent=True
	'''
	if indent:
		return [' '*node[0] + str(node[1]) for node in accum]  # node = (level, value)
	else:
		return [node[1] for node in accum]


def get_path_by_value(tree, value):
	'''
	A search routine. Look for the value in the tree.
	Return the path to the node: e.g., ['left', 'left', 'value'].
	When the value is not found, the last element in the path is None (i.e., path[-1] == None)
	'''
	path = []

	def _inner(tree, value):
		if tree['value'] == value:                             # Found you.
			path.append('value')
		elif tree['value'] > value and 'left' in tree:         # node's value is larger than value AND there's a left key ==> GOTO left
			path.append('left')
			_inner(tree['left'], value)
		elif tree['value'] < value and 'right' in tree:        # node's value is smaller than value AND there's a right key ==> GOTO right
			path.append('right')
			_inner(tree['right'], value)
		else:
			path.append(None)

	_inner(tree, value)
	return path


def get_object_from_path(obj, path):
	'''
	Auxiliary function to get the object from the tree path (see get_path_by_value).
	
	'''
	if len(path) == 0:                                         # Empty path means no value found or no root
		return None

	for subpath in path:
		try:
			obj = obj[subpath]
		except KeyError:
			return None

	return obj


def insert(tree, value):
	'''
	Insert a new leaf to the tree. This is an __in-place__ opratation.
	if tree is empty, create a new.
	Return True if successful. If the existing value is specified, raise exception.
	'''

	json_value = {'value': value}

	if not tree:                                               # Tree is empty. Create a new root node
		tree['value'] = value
		return True
	else:
		if value < tree['value']:                              # value < root. Goto left.
			if 'left' not in tree:                             # This subtree does not have the left child
				tree['left'] = json_value                      # Add it to the tree.
				return True
			else:                                              # Has the left child. Traverse.
				insert(tree['left'], value)
		elif value > tree['value']:                            # value > root. Goto right
			if 'right' not in tree:
				tree['right'] = json_value
				return True
			else:
				insert(tree['right'], value)
		else:
			return False
			# raise ValueError('{} already exists.'.format(value))               # We assume the nodes are all unique.


def insert_from_list(tree, array):
	''' Run insert for all the array elements '''
	for value in array:
		insert(tree, value)


def delete(tree, value):
	'''
	Delete a node. 
	1) The node has no child (leaf)           ===> Just delete.
	2) The node has one child                 ===> Remove the node. Relink it's parent's link to the child.
	3) The node has two children              ===> Replace the node with the next node in 'in-order' sort (the next larger number)
	Return True when successful. False when failed (value not found)
	'''
	path = get_path_by_value(tree, value)                      # Find the path to the node.
	if len(path) == 0:                                         # No value found.
		return False

	path = path[:-1]                                           # Remove the last 'value' part. e.g., ['right', 'right', 'value'] => ['right', 'right']
	parent_obj = tree
	for p in path[:-1]:
		parent_obj = parent_obj[p]
	target_key = path[-1]

	boolean = ['left' in parent_obj[target_key], 'right' in parent_obj[target_key]]
	if all(boolean):                                           # Both left and right children are present.
		print('both children')
		current = parent_obj[target_key]

		# Look for the next node in-order 
		next_parent = current
		next_obj = current['right']
		while 'left' in next_obj:
			next_parent = next_obj
			next_obj = next_obj['left']

		current['value'] = next_obj['value']
		del next_parent['right']

	elif any(boolean):                                         # Either left or right child is present
		left_or_right = 'left' if 'left' in parent_obj[target_key] else 'right'
		print('one child on', left_or_right)
		child = parent_obj[target_key][left_or_right]
		parent_obj[target_key] = child

	else:                                                      # No child. Delete this node.
		print('No child')
		del parent_obj[target_key]


if __name__ == '__main__':
	# Read the json formatted file
	with open('./BinaryTreeSample.json', encoding='utf-8') as fp:
		tree = json.load(fp)                                   # Note: load(fp) vs loads(str)

	print('--- Testing the traversal methods ---')
	print('1) Pre-order:     ', traverse_values(traverse_preorder(tree)))
	print('2) In-ordert:     ', traverse_values(traverse_inorder(tree, 0, [])))
	print('3) Post-ordert:   ', traverse_values(traverse_postorder(tree, 0, [])))
	breadth = traverse_breadth_first(tree)	
	print('4) Breadth-first: ', traverse_values(breadth))
	print('\n'.join(traverse_values(breadth, True)))

	print('-- Testing get_path_by_value --')
	for value in [8, 10, 12, 15, 16, 20, 25, 30]:
		path = get_path_by_value(tree, value)
		print('Find {} -> Path: {}, Depth: {}, Value: {}'.format(value, path, len(path)-1, get_object_from_path(tree, path)))

	print('--- Testing insertion ---')
	new_tree = {}
	insert(new_tree, 15)                                                       # root node
	insert_from_list(new_tree, [10, 12, 8, 20, 16, 25, 30])                    # add the rest and alsoa new node "30"
	print(json.dumps(new_tree, indent=2))
	print('2) In-order:     ', traverse_values(traverse_inorder(new_tree, 0, [])))

	print('--- Testing deletion ---')
	delete(new_tree, 8)                                                        # Checking the end leaf
	print('8 deleted\n', json.dumps(new_tree, indent=2))
	delete(new_tree, 25)                                                       # Checking the node with one child
	print('25 deleted\n', json.dumps(new_tree, indent=2))
	delete(new_tree, 20)                                                       # Two children
	print('20 deleted\n', json.dumps(new_tree, indent=2))

