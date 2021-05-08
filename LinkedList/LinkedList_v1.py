#!/usr/bin/env python
# 2021-04-11: ST

import math

# Represents a single element. It contains its value and the link (object ID) to the next element.
class Element:

    # Constructor for an element
    def __init__(self, val):
        self.value = val                                       # the value of the element
        self.next = None                                       # Next Element

    # Implement toString
    def __str__(self): 
        str_next = 'None'
        if self.next != None:
            str_next = id(self)
        return ('%s, %s' % (self.value, str_next))


# A class to control the entire list.
# This is the first element. If self.head is None, no member.
class LinkedList:

    # Create an empty list
    def __init__(self):
        self.head = None                                      


    # tostring
    def __str__(self):
        return str(self.toList())

    # Iterator
    def __iter__(self):
        return self

    def __next__(self):
        if self.next == None:
            raise StopIteration



    # Convert the Linked list to an array
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


    # Search for the element with the same value. It also counts the positinal number.
    # To look for the end, specify math.nan (should not be equal to any value)
    # Returns:
    #  1) [0, None] when the LinkedList is empty
    #  2) [count, Element instance], otherwise (return the last element if the Nan is specified ... for appending)
    def search(self, target_value):
        if self.head == None:                                  # This list is empty
            return [0, None]

        next_element = self.head                               # Start looking from the head
        count = 0
        while next_element.value != target_value:              # Look for the target value
            count = count + 1
            if next_element.next == None:                      # Looked up to the end but I couldn't find it.
                break
            else:
                next_element = next_element.next

        return [count, next_element]


    # Return the number of elements. Look for the last element.
    def size(self):
        count, _ = self.search(math.nan)
        return count


    # Insert the new value 'newval' AFTER the first element with the value 'lookfor'.
    # To append to the last, specify NaN to 'lookfor'.
    # Return the element appended.
    def insert(self, newval, lookfor=math.nan):
        new_element = Element(newval)                          # Element to add

        count, next_element = self.search(lookfor)             # Look for NaN (return the last)

        if next_element == None:                               # The list is empty. Change the head.
            self.head = new_element
        else:
            if next_element.next != None:                      # Insertion requires to change the new_element's next to the prvious next.
                new_element.next = next_element.next
            next_element.next = new_element

        return new_element

    # Syntax sugar
    def append(self, newval):
        return self.insert(newval)


    # Insert an element with the value 'new_val' next to the first alement found with the value 'next_val'
    # When there is no such element

    # Delete the first element that has the value specified.
    # To delete, you need to know the previous element too. My search is not designed to provide that information, hence it does loop here.
    # Returns False if the element is not found. Otherwise True.
    def delete(self, val):
        if self.head == None:                                  # Empty list. Return.
            return False

        prev_element = None
        current_element = self.head

        # Check if the first element is the only element and has the 'val'. If so, modify the head.
        if current_element.next == None and current_element.value == val:
            self.head = None
            return True

        while True:
            if current_element.value == val:                   # I found the 'val'
                if prev_element == None:                       # I am the first element. Modify the head.
                    self.head = current_element.next
                else:                                          # Othewise, somewhere in the middle (or last)
                    prev_element.next = current_element.next
                return True
            prev_element, current_element = current_element, current_element.next


        return False


### Test
if __name__ == '__main__':
    # Testing Element
    test_element = Element(100)
    print(test_element)
    test_element = Element(math.nan)
    print(test_element)

    # New linked list
    linkedList = LinkedList()

    # Testing append
    for i in range(0, 20, 2):
        linkedList.append(i)
    print('%d: %s' % (linkedList.size(), linkedList))

    # Testing insert. To the first (0), middle(10) and the last(18)
    linkedList.insert(1, 0)
    linkedList.insert(11, 10)
    linkedList.insert(19, 18)
    print('%d: %s' % (linkedList.size(), linkedList))

    # Testing delete First (0), Middle(11), Last(19)
    linkedList.delete(0)
    linkedList.delete(11)
    linkedList.delete(19)
    print('%d: %s' % (linkedList.size(), linkedList.toList()))

