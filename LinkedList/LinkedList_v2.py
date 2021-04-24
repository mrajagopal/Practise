#!/usr/bin/env python
# 2021-04-11: ST. Version 2:
#  - Search returns both previous and current elements (prev for deletion)
#  - Insert is only for insertion. Does not append.

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


    def __search(self, lookfor=math.nan):
        '''
        Look for the first element with the value 'lookfor'.
        This is a private method used by other public methods.

        Returns: [count, isFound, prev_element, target_element]
        - count: a number of elements (int)
        - isFound: True if the target value is found. Used for discerning between 1) Found it in the end element vs 2) Not found
        - prev_element: None if there is only one element.
        - target_element: The element that contains the tartget value.

        Use math.nan for lookfor to search to the end without finding anything (for size and append)
        '''
        prev_element = None
        this_element = self.head                               # None if no element
        count = 0
        isFound = False                                     

        if self.head != None:                                  # I have at least one element to search
            count = 1
            while True:
                if this_element.value == lookfor:              # I found you.
                    isFound = True
                    break
                if this_element.next == None:                  # Reached the last element. Break.
                    break

                prev_element = this_element
                this_element = this_element.next
                count += 1

        return [count, isFound, prev_element, this_element]


    # You can 'insert' next to the last element
    def insert(self, lookfor, newval):
        _, isFound, _, this_element = self.__search(lookfor)

        if isFound == False:                                   # Either the link is empty or the lookfor is not present
            return '{} could not be inserted because {} is not there.'.format(newval, lookfor)

        print("Found ", this_element)
        new_element = Element(newval)
        new_element.next = this_element.next
        this_element.next = new_element
        return '{} inserted next to {}.'.format(newval, lookfor)


    def append(self, newval):
        new_element = Element(newval)
        if self.head == None:                                  # Adding the first element
            self.head = new_element
            count = 0
        else:
            count, isFound, _, this_element = self.__search()        # Look for non-existing value
            if isFound == True:                                # Something must be wrong.
                raise Exception('Coding error in append.')
            this_element.next = new_element

        return '{}-th element {} added.'.format(count, newval)


    def size(self):
        count, _, _, _ = self.__search()
        return count


    def delete(self, lookfor):
        '''
        Delete the element with the value 'lookfor'.
        If the 'lookfor' is not found, it does not alter the linked list.
        '''
        _, isFound, prev_element, this_element = self.__search(lookfor)

        if isFound == False:                             # No element found OR there is no element. Return False.
            return '{} could not be deleted because it is not there.'.format(lookfor)

        if prev_element == None:                         # This is the first element
            if this_element.next == None:                # Only element
                self.head = None
                return '{} deleted. The list became empty.'.format(lookfor)
            else:
                self.head = this_element.next
                return '{} deleted. It was the first elment.'.format(lookfor)

        if this_element.next == None:                    # This is the last element. Delete.
            prev_element.next = None
            return '{} deleted. It was the last element.'.format(lookfor)

        prev_element.next = this_element.next
        return '{} deleted.'.format(lookfor)


    def print(self):
        '''
        Non iterator version.
        print the total number of elements and each element (value, its object ID, the next Element object ID).
        The next ID is None when the element is the last one.
        '''
        count = linkedList.size()
        print('Total {}'.format(count))
        if count == 0:
            return

        next_element = linkedList.head
        while True:
            print(next_element)
            if next_element.next == None:
                break
            next_element = next_element.next


##### Test me #####
if __name__ == '__main__':
    linkedList = LinkedList()                                  # Make me (empty)
    for newval in [2, 5, 7]:                                   # Add three [2, 5, 7]
        print('Append 3\n', linkedList.append(newval))
    linkedList.print()

    #                       ok(1st)  ok(last) fail
    for lookfor, newval in [(2, 3),  (7, 11), (13, 17)]:       # Insert three. One fails [2, 3, 5, 7, 11]
        print('Insert 3. 1 fail\n', linkedList.insert(lookfor, newval))
    linkedList.print()

    for lookfor in [2, 5, 17]:                             # Remove three. One fails [3, 7, 11]
        print('Delete 3. 1 fail\n', linkedList.delete(lookfor))
    linkedList.print()
