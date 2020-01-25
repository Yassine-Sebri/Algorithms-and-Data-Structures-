"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
"""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """
        This method increments through the entire linked list,
        Making it less efficient than other structures when simply
        adding to the end.
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_element(self, position):
        """
        Provide position (int) and find element at that position.
        Increments through the list until it finds element at that position.
        """
        i = 0
        current = self.head

        while position > i:
            if current.next:
                current = current.next
            else:
                return None
            i += 1

        return current

    def get_position(self, value):
        """
        Provide value to return position of value if found.
        Returns None if not found.
        """
        i = 0
        current = self.head

        while value != current.value:
            if current.next is not None:
                current = current.next
            else:
                return None
            i += 1
        return i

    def insert(self, new_element, position):
        """
        Insert new element at position (int).
        """
        if position == 0:
            new_element.next = self.head
            self.head = new_element
        else:
            prev = self.get_element(position - 1)
            new_element.next = prev.next
            prev.next = new_element

    def delete(self, value):
        """
        Delete the first node with a given value.
        """
        if self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while value != current.value:
                prev = current
                current = current.next
            prev.next = current.next


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should print 2
print(ll.get_position(3))
print()

# Test insert
ll.insert(e4, 2)
# Should print 2
print(ll.get_position(4))
print()

# Test delete
ll.delete(2)
# Should print 0
print(ll.get_position(1))
# Should print 1
print(ll.get_position(4))
# Should print 2
print(ll.get_position(3))
