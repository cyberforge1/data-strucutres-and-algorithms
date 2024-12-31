# data_structures/array.py

# Array data structure implementation.
# Provides basic operations such as access, insertion, deletion, and traversal.
# Time Complexity:
# - Access: O(1)
# - Insertion: O(n) (worst case, due to shifting elements)
# - Deletion: O(n) (worst case, due to shifting elements)
# - Traversal: O(n)

class Array:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum capacity of the array
        self.size = 0             # Current number of elements in the array
        self.data = [None] * capacity  # Fixed-size array initialized with None

    def insert(self, index, value):
        if self.size >= self.capacity:
            raise OverflowError("Array is full")
        if index < 0 or index > self.size:
            raise IndexError("Invalid index")
        
        # Shift elements to the right to make space
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[index] = value
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")
        
        # Shift elements to the left to fill the gap
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        
        self.data[self.size - 1] = None
        self.size -= 1

    def access(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")
        return self.data[index]

    def traverse(self):
        return [self.data[i] for i in range(self.size)]
