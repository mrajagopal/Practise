#!/usr/bin/env python
# 2021-05-01: Cicurlar Linked List (unidirectional)

import math

class Element:

    def __init__(self, val):
        ''' By default, it points to itself.'''
        self.value = val
        self.next = None

    def __str__(self):
        next_id = 'None'
        if self.next != None:
            next_id = id(self.next)
        return '(V{}, S{}, N{})'.format(self.value, id(self), next_id)


class LinkedListCircular:
    '''
    The last element points to the first element.
    The first element is stored in self.head.
    In a loop, the current poistion is stored in self.current (loop counter). Exit from the loop when the current element is equal to the head.
    '''

    def __init__(self):
        self.head = None
        self.current = None

    def __str__(self):
        head_id = 'None'                                 # When the list is empty
        current_id = 'None'                              # When the iteration is initialized
        if self.head != None:
            head_id = id(self.head)
        if self.current != None:
            current_id = id(self.current)
        return '(H{}, C{})'.format(head_id, current_id)

    def __iter__(self):
        # print('--iterator initialized')
        self.current = None                              # Reset the iterator
        return self

    def __next__(self):
        if self.head == None:                            # There is no element. Don't iterate.
            # print('next: nothing to iterate', self)
            raise StopIteration
        elif self.current == None:                       # 1st iteration
            self.current = self.head.next                # Next current element is the head's next.
            # print('next: first', self)
            return self.head
        elif self.current == self.head:                  # The current element is head. Circuled around the entire list. Exit.
            # print('next: reached end', self)
            raise StopIteration
        else:
            current = self.current 
            self.current = self.current.next             # Next current element is the current's next.
            # print('next: otherwise', self)
            return current

    def __len__(self):
        count = 0
        for elem in self:
            count += 1
        return count

    def __del__(self):
        self.head = None


    def __lookfor(self, lookfor):
        '''
        Private method to look for the first element with the value 'lookfor' (start looking from the head).
        Returns the Elements found plus the one before (previous is needed for deletion).
        Returns None if 1) No element (head == None) or 2) 'lookfor' is not found.
        '''
        if self.head == None:                            # There is no element to look for. Return None.
            return None

        current = None

        # Find the last element - the previous element of the head
        for elem in self:
            pass
        prev = elem

        if self.head != None:
            for elem in self:
                if elem.value == lookfor:
                    current =  elem
                    break
                prev = elem

        if current == None:                              # Could not find.
            return None

        return {'prev': prev, 'current': current}


    def append(self, val):
        '''
        Append next to the last element.
        For the first element, modify self.head. At this stage, the element points to itself.
        Returns the element inserted.
        '''
        new_element = Element(val)
        if self.head == None:                            # 1st item
            # print('append 1st')
            new_element.next = new_element               # points to itself.
            self.head = new_element
        else:
            for elem in self:                            # Scan toward the end
                # print('loop: ', elem)
                pass
            new_element.next = self.head
            elem.next = new_element

        return new_element


    def delete(self, lookfor):
        '''
        Delete the first element with the value 'lookfor'. Returns the deleted object. None when not found.
        '''
        del_element = None

        elems = self.__lookfor(lookfor)
        if elems != None:
            if len(self) == 1:                           # Deleting the one-and-only element. Empty the list
                self.head = None
                self.current = None
            else:
                elems['prev'].next = elems['current'].next
                if elems['current'] == self.head:              # Deleting the head element
                    self.head = elems['current'].next
            del_element = elems['current']

        return del_element


    def insert(self, lookfor, newval):
        '''
        Inseert a new element with 'newval' next to (to the right) the element with the lookfor.
        Returns the inserted object.
        Returns None when the lookfor element is not found.
        Note: Can't insert to the top of the list (inserting next (right) to the last element).
        '''
        elems = self.__lookfor(lookfor)                  # No element in the list. Return None.
        if elems == None:
            return None

        new_element = Element(newval)
        new_element.next = elems['current'].next
        elems['current'].next = new_element
        return new_element


if __name__ == '__main__':
    llc = LinkedListCircular()

    print('Appending ...')                               # [2, 3, 5, 7, 11]    
    for val in [2, 3, 5, 7, 11]:
        llc.append(val)
    for elem in llc:
        print('...', elem)

    print('Deleting ...')                                # [3, 5, 7]
    for val in [2, 11, 13, math.nan]:
        elem = llc.delete(val)
        print(val, elem)
    for elem in llc:
        print('...', elem)

    print('Inserting ...')
    for lookfor, newval in [(3, 4), (7, 1), (13, 10)]:  # [3, 4, 5, 7, 1]
        elem = llc.insert(lookfor, newval)
        print('Next to {}. Insert {}. {}'.format(lookfor, newval, elem))
    for elem in llc:
        print('...', elem)
