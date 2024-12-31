# data_structures/hash_table.py

# Hash Table implementation using open addressing with linear probing for collision resolution.
# Provides basic operations such as insertion, deletion, and searching.
# Time Complexity:
# - Insertion: O(1) (average case), O(n) (worst case due to collisions)
# - Search: O(1) (average case), O(n) (worst case due to collisions)
# - Deletion: O(1) (average case), O(n) (worst case due to collisions)

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity  # Fixed size of the hash table
        self.size = 0             # Current number of elements in the table
        self.table = [None] * capacity  # Initialize the table with None

    def _hash(self, key):
        """Compute the hash value for a given key."""
        return hash(key) % self.capacity

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        if self.size >= self.capacity:
            raise OverflowError("Hash table is full")
        
        index = self._hash(key)

        # Linear probing for collision resolution
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.capacity
        
        if self.table[index] is None:
            self.size += 1
        self.table[index] = (key, value)

    def search(self, key):
        """Search for a value by its key."""
        index = self._hash(key)

        # Linear probing to find the key
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]  # Return the associated value
            index = (index + 1) % self.capacity
        
        return None  # Key not found

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash(key)

        # Linear probing to find the key
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None  # Remove the key-value pair
                self.size -= 1
                return True
            index = (index + 1) % self.capacity
        
        return False  # Key not found
