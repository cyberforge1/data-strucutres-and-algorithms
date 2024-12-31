# search/bfs.py

# Breadth-First Search (BFS) algorithm for traversing or searching graph data structures.
# BFS explores all neighbors of a node before moving to the next level.
# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
# Space Complexity: O(V) for storing visited nodes and the queue.

def bfs(graph, start):
    visited = set()  # Track visited nodes
    queue = [start]  # Initialize the queue with the starting node
    traversal_order = []  # List to store the order of traversal

    while queue:
        current = queue.pop(0)  # Dequeue the first element

        if current not in visited:
            visited.add(current)
            traversal_order.append(current)

            # Enqueue all unvisited neighbors
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order
