# data_structures/linked_list.py

# Singly Linked List implementation.
# Provides basic operations such as insertion, deletion, and traversal.
# Time Complexity:
# - Insertion: O(1) at the head, O(n) at the tail (without a tail pointer)
# - Deletion: O(1) if the node is known, O(n) to find the node
# - Traversal: O(n)

class Node:
    def __init__(self, value):
        self.value = value  # Value of the node
        self.next = None    # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the list with no head node

    def insert_at_head(self, value):
        """Insert a new node at the head of the list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, value):
        """Insert a new node at the tail of the list."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete(self, value):
        """Delete the first node with the given value."""
        current = self.head
        previous = None

        while current is not None:
            if current.value == value:
                if previous is None:  # Deleting the head node
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False  # Value not found

    def search(self, value):
        """Search for a node with the given value."""
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def traverse(self):
        """Return a list of all values in the linked list."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result
