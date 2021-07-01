#!/usr/bin/env python
# 2021-07-01: binaretree module (pip install binarytree)
#   See
#    PYPI: https://pypi.org/project/binarytree/
#    API Doc: https://binarytree.readthedocs.io/en/main/specs.html
#    This one is good for deletion: https://www.delftstack.com/ja/tutorial/data-structure/binary-search-tree-delete/
#
# Note: Binary Search Tree (BST) = 二分探索木

import binarytree as bt
import math

my_list = [15, 10, 20, 8, 13, 16, 25]                                          # List must be in breadth first order
root = bt.build(my_list)                                                       # Returns the root node of the tree
print('** Create a BST from {} **'.format(my_list))
print(root)

# print just values
print('values in breadth-first traversal: {}'.format(root.values))             # breath-first order

# len(root): A number of nodes
# root.height: Counted from 0 (i.e., root-only's height is 0)
print('type: {}, len: {}, height: {}'.format(type(root), len(root), root.height))

# max and min
print('max: {}, min: {}'.format(root.max_node_value, root.min_node_value))

# Only leaves:
print('leaves: {}, count: {}'.format(root.leaves, root.leaf_count))

# Check the types of the tree
print('** Tree types **')
for x in ['balanced', 'bst', 'complete', 'max_heap', 'min_heap', 'perfect', 'strict', 'symmetric']:
    is_x = 'is_' + x
    print('- {}: {}'.format(x, root.properties[is_x]))


# Each traversal order property returns a list of the Node classes. 
# To access the value of the Node, use [0]. ([1] is for left, [2] is for right)
print('** Traversal order **')
for style in ['preorder', 'inorder', 'postorder', 'levelorder']:
    tmp = []
    traversal_list = getattr(root, style)
    value_list = [node.value for node in traversal_list]
    print('- {}: {}'.format(style, value_list))



# The library does not come with an insert method: Write my own.
# 
def insert(self, value):
    new_node = bt.Node(value)

    def _inner(node):
        if value < node.value:                                 # Goto Left
            if node.left == None:
                node.left = new_node
            else:
                _inner(node.left)
        elif value > node.value:                               # Goto right
            if node.right == None:
                node.right = new_node
            else:
                _inner(node.right)

    _inner(self)
    return

setattr(bt.Node, 'insert', insert)

# Insertion makes None nodes
print('** Test inserting nodes **')
for val in [11, 30, 29, 40, 12]:
    root.insert(val)
print(root)
print(root.values)

# Iterator does not yield the skipped nodes.
print(list(root))



# Also not with a search method.
#
def search(self, value):
    '''
    Returns a tuple with (Node object, its level-order index). The index is needed for __getitem__, __delitem__ and __setitem__.
    (None, None) if not found.
    '''
    def _inner(node, pos):
        if value == node.value:
            return (node, pos)
        elif value < node.value and node.left != None:         # Goto Left
            return _inner(node.left, 2*pos+1)
        elif value > node.value and node.right != None:        # Goto Right
            return _inner(node.right, 2*pos+2)
        else:
            return (None, None)

    return _inner(self, 0)

setattr(bt.Node, 'search', search)

# Convinience function: Find the location (level, horizontal position) from the index.
# Both counted from 0.
#
def get_location_from_pos(pos):
    if pos == None:
        return (None, None, None)
    level = math.floor(math.log2(pos + 1))
    horizon = (pos + 1) - 2 ** level
    left_or_right = 'left' if pos % 2 == 1 else 'right'
    return (level, horizon, left_or_right)


print('** Test searching nodes **')
for val in [11, 12, 30, 40, 100]:
    node, pos = root.search(val)
    found = node.value if node != None else None
    print('searching {} ... Found {} at {}: {}'.format(val, found, pos, get_location_from_pos(pos)))


# The original __delitem__() deletes the node and all its children.
# Implement my version.
#
def delete(self, value):
    target_node, target_pos = self.search(value)                               # Look for the node to delete

    # The node to delete is root. I chose not to delete.
    if target_pos == 0:
        print('Cannott remove root')
        return False

    # Not found. Return immediately
    if target_node == None:
        print('DEBUG: {} not found. No action.'.format(value))
        return False
    print('DEBUG: {} found at {}.'.format(value, target_pos))

    # Check if the target has 1) No, 2) One, 3) Two children.
    boolean = [target_node.left == None, target_node.right == None]

    # No child. Just remove.
    if all(boolean):
        print('DEBUG: No child (leaf). Delete this.')
        del self[target_pos]
        return True

    # Left or right node can be accessed from Node[pos][toggle], where toggle = 1 for Left, and = 2 for Right (0 for itself: value)
    left_or_right = ['value', 'left', 'right']                                 # For string printing

    # Determine parent's position.
    daddy_pos = (target_pos - 1) // 2                                          # Don't know if I am on left or right at this stage.
    daddy_toggle = 1 if self[daddy_pos].value > value else 2
    print('DEBUG: Daddy at {}. I am a {} child.'.format(daddy_pos, left_or_right[daddy_toggle]))

    # One child (either left or right)
    if any(boolean):
        # Determine child's position
        child_toggle = 1 if target_node.left != None else 2
        child_pos = target_pos * 2 + child_toggle
        print('DEBUG: One child at {}({}). Replace the target with the child.'.format(child_pos, left_or_right[child_toggle]))

        # Replace the target with the child
        self[daddy_pos][daddy_toggle] = self[child_pos]
        return True

    # Two children.
    if target_node.right.left == None:
        # And the right child only has right child (grandchild). Swap this right with the target.
        print('DEBUG: Two children. My right child is the one to replace with.')
        self[daddy_pos][daddy_toggle] = target_node.right
        target_node.right.left = target_node.left
        return True
    else:
        # Two children. Generic
        next_inorder = target_node.right
        next_inorder_pos = target_pos * 2 + 2
        while next_inorder.left != None:
            next_inorder = next_inorder.left
            next_inorder_pos = next_inorder_pos * 2 + 1                        # next left
        print('DEBUG: Two children. The next inorder node at {}.'.format(next_inorder_pos))
        target_node.value = next_inorder.value
        del self[next_inorder_pos]
        return True

setattr(bt.Node, 'delete', delete)

print('** Test deleting nodes **')
for sample, target in [
    ([15, 8, 20, 4, 10, 16, 25], 4),
    ([15, 8, 20, 4, None, 16, 25, 2, 5], 8),
    ([15, 8, 20, None, 10, 16, 25, None, None, 9, 11], 8),
    ([15, 8, 20, 4, None, 16, 25, None, None, None, None, None, None, None, 30], 20),
    ([15, 8, 20, 4, 10, 18, 25, None, None, None, None, 16, 19, 22, 30], 20)
]:
    tree = bt.build(sample)
    print(tree)
    tree.delete(target)
    print(tree)