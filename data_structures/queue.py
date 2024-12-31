# data_structures/queue.py

# Queue implementation using a circular buffer.
# Provides basic operations such as enqueue, dequeue, and checking the queue's state.
# Time Complexity:
# - Enqueue: O(1)
# - Dequeue: O(1)
# - Peek: O(1)

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum size of the queue
        self.data = [None] * capacity  # Fixed-size array to store elements
        self.head = 0  # Index of the front element
        self.tail = 0  # Index of the next available slot
        self.size = 0  # Current number of elements in the queue

    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0

    def is_full(self):
        """Check if the queue is full."""
        return self.size == self.capacity

    def enqueue(self, value):
        """Add an element to the end of the queue."""
        if self.is_full():
            raise OverflowError("Queue is full")
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity  # Circular increment
        self.size += 1

    def dequeue(self):
        """Remove and return the element at the front of the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.data[self.head]
        self.data[self.head] = None  # Clear the slot
        self.head = (self.head + 1) % self.capacity  # Circular increment
        self.size -= 1
        return value

    def peek(self):
        """Return the element at the front of the queue without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.data[self.head]
