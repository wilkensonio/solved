"""
has path
Write a function, has_path, that takes in a dictionary representing
 the adjacency list of a directed acyclic graph and two nodes (src, dst).
  The function should return a boolean indicating whether or not there exists a
   directed path between the source and destination nodes.

Hey. This is our first graph problem, so you should be liberal
 with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ
"""
from collections import deque


# def has_path(graph, src, dst):
#     queue = deque([src])
#     while queue:
#         current = queue.popleft()
#
#         if current == dst:
#             return True
#
#         for neighbor in graph[current]:
#             queue.append(neighbor)
#     return False


def has_path(graph, src, dst):
    if src == dst:
        return True
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst):
            return True
    return False


# def has_path(graph, src, dst):
#     stack = [src]
#     while stack:
#         current = stack.pop()
#         if current == dst:
#             return True
#         for neigh in graph[current]:
#             stack.append(neigh)
#     return False


# def has_path(graph, src, dst):
#   queue = deque([src])
#   while queue:
#     node = queue.popleft()
#     if node == dst:
#       return True
#     for neighbor in graph[node]:
#       queue.append(neighbor)
#   return False

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

print(has_path(graph, 'f', 'j'))  # False
