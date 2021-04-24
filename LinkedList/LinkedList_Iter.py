#!/usr/bin/env python
# 2021-04-24: ST. Iterator edition

import math

class Element:
    """
    Represents an element in an array.
    The first element is referenced from LinkedList object's head property.    
    When the 'next' property is None when it is the last element. Otherwise a reference to the next Element.
    """
    def __init__(self, val):
        if isinstance(val, int) == False:                      # Currently only supports integer
            raise TypeError('Only integers.')
        self.value = val                                       # The value of the element
        self.next = None                                       # Next Element

    def __str__(self):
        next_id = "None"
        if self.next != None:
            next_id = id(self.next)
        return '({}, {}, {})'.format(self.value, id(self), next_id)


class LinkedList:

    def __init__(self, element=None):                          # Constructor. Create an empty list
        self.head = None                                       # Pointer to the first element
        self.current = None                                    # Pointer to the current element in iterator


    def __del__(self):                                         # Destructor
        self.head = None


    def __iter__(self):                                        # Iterator
        self.current = self.head                               # Initialize the current pointer to the first element.
        return self


    def __next__(self):                                        # Iterator's Next
        current = self.current
        if current == None:                                    # No more element.
            self.current = self.head
            raise StopIteration
        self.current = self.current.next
        return current


    def __len__(self):
        count = 0
        for elem in self:
            count += 1
        return count


    # Append always succeeds
    def append(self, newval):
        new_element = Element(newval)
        if self.head == None:                                  # The first element
            self.head = new_element
        else:
            for elem in self:                                  # Can't loop if there is no element
                pass
            elem.next = new_element                            # Add to the last.

        return True


    # When the list is empty, you can't insert. Use append
    def insert(self, lookfor, newval):
        if self.head == None:                                  # No element yet. Search should fail.
            return False

        new_element = Element(newval)
        for elem in self:
            if elem.value == lookfor:
                if elem.next == None:                          # This is the last one. Append to the last.
                    elem.next = new_element
                else:                                          # Otherwise, insert in between
                    elem.next = new_element
                    new_element.next = next(self)
                return True
        
        return False


    def delete(self, lookfor):
        if self.head == None:                                  # Can't delete anything when empty
            return False

        previous = None
        for elem in self:
            if elem.value == lookfor:
                try:                                           # Need the next item
                    nextOne = next(self)
                except StopIteration:                          # No next itme. This is the last one.
                    nextOne = None
                if previous == None:                           # Delete the first item
                    self.head = nextOne
                else:
                    previous.next = nextOne
                return True
            previous = elem

        return False


    def size(self):
        return len(self)


    def print(self):
        print('Count: {}'.format(len(self)))
        for elem in self:
            print(elem)


##### Test me #####
if __name__ == '__main__':
    print('-- LinkedList iterator version --')
    linkedList = LinkedList()                                  # Make me (empty)

    for newval in [2, 5, 7]:                                   # Add three [2, 5, 7]
        linkedList.append(newval)
    linkedList.print()

    #                       ok(1st)  ok(last) fail
    for lookfor, newval in [(2, 3),  (7, 11), (13, 17)]:       # Insert three. One fails [2, 3, 5, 7, 11]
        linkedList.insert(lookfor, newval)
    linkedList.print()

    for lookfor in [2, 5, 17]:                                 # Remove three. One fails [3, 7, 11]
        linkedList.delete(lookfor)
    linkedList.print()
