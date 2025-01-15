# data_structures/doubly_linked_list.py

# Doubly Linked List implementation.
# Provides basic operations such as insertion, deletion, and traversal.
# Time Complexity:
# - Insertion: O(1) at the head or tail
# - Deletion: O(1) if the node is known, O(n) to find the node
# - Traversal: O(n)
# - Reverse Traversal: O(n)

class Node:
    def __init__(self, value):
        self.value = value  # Value of the node
        self.next = None    # Pointer to the next node
        self.prev = None    # Pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the list with no head node
        self.tail = None  # Initialize the list with no tail node

    def insert_at_head(self, value):
        """Insert a new node at the head of the list."""
        new_node = Node(value)
        if self.head is None:  # List is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_tail(self, value):
        """Insert a new node at the tail of the list."""
        new_node = Node(value)
        if self.tail is None:  # List is empty
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, value):
        """Delete the first node with the given value."""
        current = self.head

        while current is not None:
            if current.value == value:
                # Update pointers for deletion
                if current.prev:  # Not the head
                    current.prev.next = current.next
                else:  # Head node
                    self.head = current.next
                
                if current.next:  # Not the tail
                    current.next.prev = current.prev
                else:  # Tail node
                    self.tail = current.prev
                
                return True
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
        """Return a list of all values in the linked list (from head to tail)."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def traverse_reverse(self):
        """Return a list of all values in the linked list (from tail to head)."""
        result = []
        current = self.tail
        while current is not None:
            result.append(current.value)
            current = current.prev
        return result
