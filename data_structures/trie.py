# data_structures/trie.py

# Trie (Prefix Tree) implementation for storing and searching strings efficiently.
# Provides operations such as insertion, search, and prefix matching.
# Time Complexity:
# - Insertion: O(m), where m is the length of the word.
# - Search: O(m), where m is the length of the word.
# - StartsWith: O(m), where m is the length of the prefix.

class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Flag to indicate end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root of the trie

    def insert(self, word):
        """Insert a word into the trie."""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        """Search for a word in the trie. Returns True if found, else False."""
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        """Check if there is any word in the trie that starts with the given prefix."""
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
