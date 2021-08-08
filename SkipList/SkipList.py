#!/usr/bin/env python
# 2021-07-22

import random
import inspect

# Number of maximum lanes in this skip list. Fixed.
max_lanes = 4

# Debugger
DEBUG = True


def print_debug(*args):
    if DEBUG:
        caller = inspect.stack()[1].function                   # Pyuthon 3.5+
        print('DEBUG ({}): {}'.format(caller, args))


def id_to_hexstring(object):
    '''
    Returns the hex string respresentation of the object ID. If the targer is None, return 'None'.
    '''
    return hex(id(object)) if object != None else 'None'


def determine_lanes(max_lanes=max_lanes):
    '''
    Determine node's number of lanes stochastically.
    One lane: 50%
    Two lanes: 25%
    Three lanes: 12.5% ....
    '''
    dist = [1 - 2 ** -p for p in range(1,max_lanes+1)]         # [0.5, 0.75, 0.875, ....]
    rand = random.random()                                     # [0, 1)
    nLanes = max_lanes - 1
    for i in range(max_lanes):
        if rand < dist[i]:
            nLanes = i
            break
    print_debug(dist, rand, nLanes)
    return nLanes


class Node:

    def __init__(self, val, nLanes=None):
        '''
        Create a node with multiple lanes.
        By default, the number of lanes is determined stochastically by the 'determine_lanes' function
        unless the 'nLanes' is specified (this is for the head that must have all the lanes).
        '''
        self.nLanes = nLanes if nLanes else determine_lanes()
        self.value = val
        self.next = [None] * self.nLanes


    def __str__(self):
        if self == None:
            return 'None'
        ids = [id_to_hexstring(next_node) for next_node in self.next]
        return '({}, {}, {}, {})'.format(id_to_hexstring(self), self.value, self.nLanes, ids)


    def add_lanes(self, node_list):
        '''
        Add the next nodes to each lane.
        When the size of the node_list != nLanes, raise an error.
        '''
        if len(node_list) != self.nLanes:
            raise RuntimeError('Value {}. The size of node_list {} does not match with nLanes {}.'.format(self.value, len(node_list), self.nLanes))

        for i in range(0, self.nLanes):
            self.next[i] = node_list[i]


    def print_all(self):
        '''
        Print all the nodes starting from this node.
        '''
        node = self
        while True:
            print(node)
            if node.next[0] != None:
                node = node.next[0]
            else:
                break


    def search(self, value):
        '''
        Look for the node with the value, starting from this node.
        '''

        # When the value is smaller than the left-est node, you don't need to search further.
        if value < self.value:
            return None                                     

        current_node = self
        while True:                                            # End of list condition
            print_debug('Looking at {} lanes in {}({}) for {}'.format(current_node.nLanes, current_node.value, id_to_hexstring(current_node), value))
            if current_node.value == value:                    # Found the value
                return current_node
            elif current_node.next[0] == None:
                return None                                    # No more value

            for lane in reversed(range(current_node.nLanes)):  # Start looking from the fastest lane
                next_node = current_node.next[lane]
                print_debug('.. Lane {}'.format(lane))
                if next_node != None:                          # I have this lane.
                    if value >= next_node.value:               # Hop to the next node
                        current_node = next_node
                        break
                    elif value < next_node.value:              # Overrun. Move on to the next lane.
                        pass

        return None


class SkipList:
    '''
    I guess I don't need this as the first node is the head.
    '''
    pass


def sample():
    '''
    Create a sample skip list from the Wikipedia example.
    '''
    nodes = []
    for value, nLanes in [(1, 4), (2, 1), (3, 2), (4, 3), (5, 1), (6, 3), (7, 1), (8, 1), (9, 2), (10, 1)]:
        nodes.append(Node(value, nLanes))

    # For others
    for idx, node_list in enumerate([
        [nodes[1], nodes[2], nodes[3], None],                  # Node[0]. Value=1
        [nodes[2]],                                            # Node[1]. Value=2
        [nodes[3], nodes[3]],                                  # Node[2]. Value=3
        [nodes[4], nodes[5], nodes[5]],                        # Node[3]. value=4
        [nodes[5]],                                            # Node[4]. Value=5
        [nodes[6], nodes[8], None],                            # Node[5]. Value=6
        [nodes[7]],                                            # Node[6]. Value=7
        [nodes[8]],                                            # Node[7]. Value=8
        [nodes[9], None],                                      # Node[8]. Value=9
        [None]                                                 # Node[9]. Value=10
    ]):
        nodes[idx].add_lanes(node_list)

    return nodes[0], nodes                                     # Returns nodes[0] as the head


if __name__ == '__main__':                                     # head = nodes[0]
    head, nodes = sample()
    head.print_all()
    for lookfor in range(12):                                  # 0 and 11 should not be there
        find = head.search(lookfor)
        print('Looking for {}. Found {}'.format(lookfor, find))
