# data_structures/binary_tree.py

# Binary Tree implementation with basic operations such as insertion, traversal, and searching.
# Provides a simple structure for storing hierarchical data.
# Time Complexity:
# - Insertion: O(log n) (average case for balanced trees), O(n) (worst case for skewed trees)
# - Search: O(log n) (average case for balanced trees), O(n) (worst case for skewed trees)
# - Traversals: O(n)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the binary tree."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def search(self, value):
        """Search for a value in the binary tree."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)

    def inorder_traversal(self):
        """Perform in-order traversal of the binary tree."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current, result):
        if current is not None:
            self._inorder_recursive(current.left, result)
            result.append(current.value)
            self._inorder_recursive(current.right, result)
