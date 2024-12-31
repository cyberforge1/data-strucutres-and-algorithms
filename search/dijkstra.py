# search/dijkstra.py

# Dijkstra's algorithm for finding the shortest path from a source node to all other nodes
# in a weighted graph. Assumes all edge weights are non-negative.
# Time Complexity: O((V + E) * log V), where V is the number of vertices and E is the number of edges.
# Space Complexity: O(V + E) for storing the graph and priority queue.

import heapq  # Used for the priority queue

def dijkstra(graph, source):
    # Dictionary to track the shortest distance to each node
    distances = {node: float('inf') for node in graph}
    distances[source] = 0  # Distance to the source is 0

    # Priority queue to process nodes by shortest distance
    priority_queue = [(0, source)]  # (distance, node)

    # Dictionary to track visited nodes
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        # Update distances for all neighbors of the current node
        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                new_distance = current_distance + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances
