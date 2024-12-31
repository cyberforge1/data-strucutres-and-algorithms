# search/a_star.py

# A* algorithm for finding the shortest path in a weighted graph with a heuristic function.
# Combines the actual cost from the start and an estimated cost to the goal to prioritize nodes.
# Time Complexity: O((V + E) * log V), where V is the number of vertices and E is the number of edges.
# Space Complexity: O(V + E) for storing the graph, open list, and closed list.

import heapq  # Used for the priority queue

def a_star(graph, start, goal, heuristic):
    # Dictionary to track the actual cost to reach each node
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    # Priority queue to process nodes by their estimated total cost
    open_list = [(heuristic[start], start)]  # (f_cost, node)

    # Dictionary to track the path
    came_from = {}

    # Set to track visited nodes
    closed_list = set()

    while open_list:
        _, current = heapq.heappop(open_list)

        if current in closed_list:
            continue
        closed_list.add(current)

        # Check if the goal is reached
        if current == goal:
            return reconstruct_path(came_from, current)

        # Update costs for all neighbors of the current node
        for neighbor, weight in graph[current]:
            if neighbor in closed_list:
                continue

            tentative_g_cost = g_cost[current] + weight

            if tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current

    return []  # Return an empty path if no solution is found

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]
