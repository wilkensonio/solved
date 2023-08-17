import heapq


def dijkstra(graph, source):
    # Initialize distance array and priority queue
    distances = {node: float('infinity') for node in graph}

    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        #           0                   A
        # Ignore outdated entries in the priority queue
        if current_distance > distances[current_node]:
            #    0                          0
            continue

        # Explore neighbors and update distances
        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            # Update distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example usage:
if __name__ == "__main__":
    # Example weighted graph represented as an adjacency dictionary
    graph = {
        'A': {'B': 46, 'C': 78, 'D': 100, 'E': 50},
        'B': {'A': 46, 'C': 10},
        'C': {'A': 78, 'B': 10, 'D': 5},
        'D': {'A': 100, 'C': 5, 'E': 50, 'F': 50},
        'E': {'A': 50, 'D': 50, 'F': 70},
        'F': {'E': 70, 'D': 50}
    }
    source_node = 'A'
    shortest_distances = dijkstra(graph, source_node)
    print(shortest_distances)  # {'A': 0, 'B':46, 'C': 56, 'D': 61, 'E': 50, 'F': 111}
