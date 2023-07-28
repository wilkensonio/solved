"""
largest component
Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph.
"""


def largest_component(graph):
    visited = set()
    largest = float('-inf')

    for node in graph:
        size = explore(graph, node, visited)
        largest = max(largest, size)
    return largest


def explore(graph, node, visited):
    if node in visited:
        return 0

    visited.add(node)
    size = 1
    for neigh in graph[node]:
        if neigh not in visited:
            size += explore(graph, neigh, visited)
    return size


print(largest_component({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}))  # -> 4)
