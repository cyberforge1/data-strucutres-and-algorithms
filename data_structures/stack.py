# data_structures/stack.py

# Stack implementation using a fixed-size array.
# Provides basic operations such as push, pop, and peek.
# Time Complexity:
# - Push: O(1)
# - Pop: O(1)
# - Peek: O(1)

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum size of the stack
        self.data = [None] * capacity  # Fixed-size array to store elements
        self.top = -1  # Index of the top element in the stack

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top == -1

    def is_full(self):
        """Check if the stack is full."""
        return self.top == self.capacity - 1

    def push(self, value):
        """Add an element to the top of the stack."""
        if self.is_full():
            raise OverflowError("Stack is full")
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        """Remove and return the top element of the stack."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        value = self.data[self.top]
        self.data[self.top] = None  # Clear the slot
        self.top -= 1
        return value

    def peek(self):
        """Return the top element of the stack without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.data[self.top]
