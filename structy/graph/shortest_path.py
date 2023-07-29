"""shortest path
Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1."""

from collections import deque


def build_graph(edge_lst):
    graph = {}

    for k, v in edge_lst:
        graph.setdefault(k, []).append(v)
        graph.setdefault(v, []).append(k)
    return graph


def shortest_path(b_graph, src, dst):
    graph = build_graph(b_graph)
    visited = set(src)
    queue = deque([(src, 0)])

    while queue:
        node, dist = queue.popleft()

        if node == dst:
            return dist

        for neigh in graph[node]:
            if neigh not in visited:
                visited.add(neigh)
                queue.append((neigh, dist + 1))
    return -1


edges = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
]

# print(build_graph(edges))

print(shortest_path(edges, 'a', 'e'))

