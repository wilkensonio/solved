"""connected components count
Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.

"""


def connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore(graph, node, visited):
            count += 1

    return count


def explore(graph, node, visited):
    if node in visited:
        return False

    visited.add(node)
    for neigh in graph[node]:
        explore(graph, neigh, visited)

    return True


print(connected_components_count({
    1: [2],
    2: [1,8],
    6: [7],
    9: [8],
    7: [6, 8],
    8: [9, 7, 2]
}))
