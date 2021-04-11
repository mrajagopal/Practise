#!/usr/bin/env python
# 2021-04-11: ST Doubly Linked List

class Element:

    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None


    def toList(self):
        if self.head == None:                                  # If the list is empty,
            return []                                          # Return empty list

        ret = []
        current_element = self.head                            # Starting from head
        while True:
            ret.append(current_element.value)
            if current_element.next == None:                   # End of the list
                break
            current_element = current_element.next

        return ret


    def size(self):
        return len(self.toList())


    def addFirst(self, val):
        new_element = Element(val)
        new_element.prev = None        
        self.head = new_element


    def append(self, val):
        if self.head == None:                                  # This is the first Element
            self.addFirst(val)
            return

        new_element = Element(val)
        current_element = self.head            
        while current_element.next != None:                    # Loop to the last element
            current_element = current_element.next

        current_element.next = new_element
        new_element.prev = current_element


    # Insert to the first if there is no element
    # Insert to the ennd 
    def insert(self, val, newval):
        if self.head == None:                                  # Add as the first element
            addFirst(newval)
            return

        new_element = Element(newval)
        current_element = self.head
        while current_element.next != None and current_element.value != val:
            current_element = current_element.next

        prev = current_element.prev
        next = current_element.next        
        current_element.next = new_element                     # No need to change prev
        new_element.prev = current_element
        new_element.next = next

    # Delete
    def delete(self, val):
        if self.head == None:                                  # No element. Nothing to delete.
            return

        current_element = self.head
        if current_element.value == val:                       # Delete the 1st item
            print('Deleting the first element %d.' % val)
            self.head = current_element.next
            current_element.next.prev = None
            return

        while current_element.value != val:
            current_element = current_element.next
            if current_element == None:
                break

        if current_element == None:
            print('Element %d not found. List not modified.' % val)
            return

        prev = current_element.prev
        next = current_element.next
        prev.next = next
        next.prev = prev


### Test
if __name__ == '__main__':
    dll = DoublyLinkedList()

    # Testing append
    for i in range(0, 20, 2):
        dll.append(i)
    print('%d: %s' % (dll.size(), dll.toList()))

    for target in [2, 10, 100]:
        dll.insert(target, target+1)
    print('%d: %s' % (dll.size(), dll.toList()))

    for target in [0, 11, 100]:
        dll.delete(target)
    print('%d: %s' % (dll.size(), dll.toList()))
