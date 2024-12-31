# search/dfs.py

# Depth-First Search (DFS) algorithm for traversing or searching graph data structures.
# DFS explores as far as possible along each branch before backtracking.
# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
# Space Complexity: O(V) for storing visited nodes and the recursion stack.

def dfs(graph, start):
    visited = set()  # Track visited nodes
    traversal_order = []  # List to store the order of traversal

    def dfs_recursive(node):
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            
            # Explore all unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

    dfs_recursive(start)
    return traversal_order
