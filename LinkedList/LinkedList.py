#!/usr/bin/env python
# 2021-03-25: ST

# Represents a single element. It contains 
class Element:

    # Cpnstructor for an element
    def __init__(self, val):
        self.value = val                                       # the value of the element
        self.next = None                                       # Next Element


# A class to control the entire list
class LinkedList:

    # Create an empty list
    def __init__(self):
        self.head = None
        self.count = 0                                         # Just for convinience


    # Return the number of elements
    def size(self):
        return self.count


    # Convert the Linked list to an array
    def toList(self):
        if self.head == None:                                  # If the list is empty,
            return []                                          # Return empty list

        ret = []
        current_element = self.head                            # Starting from head
        while True:
            ret.append(current_element.value)
            self.count = self.count + 1
            if current_element.next == None:                   # End of the list
                break
            current_element = current_element.next

        return ret


    # Append an element to the end.
    def append(self, val):
        if self.head == None:                                  # The first element
            self.head = Element(val)
            self.count = 1
            return

        last_element = self.head                               # Starting from head
        while last_element.next != None:                       # Traverse to the end.
            last_element = last_element.next

        last_element.next = Element(val)
        self.count = self.count + 1


    # Delete the first element that has the value specified
    # Returns False if the element is not found. Otherwise True.
    def delete(self, val):
        if self.head == None:
            return False

        if self.head.next == None and self.head.value == val:  # It has only one element and that's what I need to delete
            self.head = None
            self.count = 0
            return True

        prev_element = None
        current_element = self.head
 
        while current_element.next != None:
            if current_element.value == val:
                if current_element.next == None:               # This is the last element. Simply remove the previous next
                    prev_element.next = None
                    self.count = self.count - 1
                    print('Got ', val)
                    return True
                else:                                          # The element has the next one
                    prev_element.next = current_element.next
                    self.count = self.count - 1
                    print('Got ', val)
                    return True
            prev_element = current_element
            current_element = current_element.next

        return False


### Test
if __name__ == '__main__':
    linkedList = LinkedList()
    for i in range(0, 20, 2):
        linkedList.append(i)
    print('%d: %s' % (linkedList.size(), linkedList.toList()))

    linkedList.delete(10)
    print('%d: %s' % (linkedList.size(), linkedList.toList()))


