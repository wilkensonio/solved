"""
undirected path
Write a function, undirected_path, that takes in a
 list of edges for an undirected graph and two nodes (node_A, node_B).
  The function should return a boolean indicating
  whether or not there exists a path between node_A and node_B.
"""


def input_process(edges):
    graph = {}
    for k, v in edges:
        graph.setdefault(k, []).append(v)
        graph.setdefault(v, []).append(k)
    return graph


# def undirected_path(edges, node_A, node_B):
#   graph = input_process(edges)
#   return has_path(graph, node_A, node_B, set())

# def has_path(graph, src, dst, visited):
#   if src == dst:
#     return True
#   if src in visited:
#     return False
#   visited.add(src)
#   for neigh in graph[src]:
#     if has_path(graph, neigh, dst, visited):
#       return True
#   return False

def undirected_path(edges, node_A, node_B):
    graph = input_process(edges)
    visited = set()
    stack = [node_A]

    while stack:
        current = stack.pop()

        if current == node_B:
            return True
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
    return False


def undirected_path_rec(graph, src, dst, visited):
    if not src:
        return None
    if src == dst:
        return True
    if src in visited:
        return False

    visited.add(src)

    for neigh in graph[src]:
        if undirected_path_rec(graph, neigh, dst, visited):
            return True
    return False


edges = [
    ('i', 'j'),
    ('k', 'i'),
    ('m', 'k'),
    ('k', 'l'),
    ('o', 'n')
]

print(undirected_path(edges, 'j', 'l'))

graph = input_process(edges)
print(undirected_path_rec(graph, 'j', 'l', set()))

from collections import deque


def build_graph(edges):
    graph = {}

    for k, v in edges:
        graph.setdefault(k, []).append(v)
        graph.setdefault(v, []).append(k)

    return graph


def undirected_path(edges, src, dst):
    graph = build_graph(edges)

    visited = set()

    if not src:
        return False

    queue = deque([src])
    while queue:
        q = queue.popleft()

        if q == dst:
            return True

        visited.add(q)

        for neighbor in graph[q]:
            if neighbor not in visited:
                queue.append(neighbor)

    return False


edges = [
    ('i', 'j'),
    ('k', 'i'),
    ('m', 'k'),
    ('k', 'l'),
    ('o', 'n')
]

print(undirected_path(edges, 'j', 'm'))
