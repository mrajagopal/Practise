#!/usr/bin/env python
# 2021-06-12: Binary Tree - Classic implementation

class Node:
    '''
    Representation of a binary node.
    A leaf has None for both left and right children.
    When initialized (new-ed), it stats from a leaf. Use append to append.
    '''
    def __init__(self, value, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

    def __str__(self):
        ''' Value, its object ID, left object ID, right object ID '''
        left = hex(id(self.leftNode)) if self.leftNode != None else None
        right = hex(id(self.rightNode)) if self.rightNode != None else None
        return '{} {} {} {}'.format(self.value, hex(id(self)), left, right)


    def append(self, val_obj, position='leftNode'):
        ''' Append a new node to this node. Successful only when the target child is None (use insert to overwrite the existing) '''
        if position not in ('leftNode', 'rightNode'):          # position must be a correct property. Otherwise, FAIL.
            return False

        if getattr(self, position) != None:                    # If the child already exists, FAIL.
            return False

        if not isinstance(val_obj, Node):                      # If val_obj is not a Node instance, create a new one.
            val_obj = Node(val_obj)

        setattr(self, position, val_obj)
        return val_obj


    @staticmethod
    def traverse(node, level=0, accum=[]):
        '''
        Return a list of all nodes starting from this node. This method implements pre-order/depth-first traversal.
        level: Represents the depth level. Used for indentation in printing.
        terminate_at: Return the first node with this value (a single element list)
        accum: Accumulate the nodes found (list).
        '''
        accum.append((level, node))
        for child in (node.leftNode, node.rightNode):
            if child != None:
                accum = Node.traverse(child, level+1, accum)

        return accum


    @staticmethod
    def print_tree(node, indentation_char=' '):
        ''' Print the tree from the given node.'''
        tree = Node.traverse(node, accum=[])
        for level, node in tree:
            print('{}{}'.format(indentation_char*level, node))


    @staticmethod
    def look_for(node, value):
        '''
        Return the first node with the value specfied (depth-first) and its parent. None if none found.
        The logic is identical to 'traverse': It's just that this returns immediately when it finds the value.
        '''
        if node.value == value:
            return node

        ret = None
        for child in (node.leftNode, node.rightNode):
            if child != None: 
                ret = Node.look_for(child, value)
                if ret != None:
                    break

        return ret

        
    @staticmethod
    def delete(node, value):
        ''' Delete the first node found (via look_for). All the nodes below this node is deleted. '''
        node_found = look_for(node, value)
        if node_found == None:                                 # The target not found
            return None



# Test
if __name__ == '__main__':
    # Creating the test tree
    root = Node(15)
    left = root.append(10)
    left.append(8)
    left.append(12, 'rightNode')
    right = root.append(20, 'rightNode')
    right.append(16)
    right.append(25, 'rightNode')

    # traversal test
    print('Testing traverse ...')
    tree = Node.traverse(root, accum=[])
    for level, node in tree:
        print(level, node)

    # print test
    print('Testing print_tree ...')
    Node.print_tree(root)

    # Look for test
    print('Testing look_for ...')
    for value in [15, 10, 16, 12, 100]:
        found = Node.look_for(root, value)
        print('Found {} in ==> {}'.format(value, found))

