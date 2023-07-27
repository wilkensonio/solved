from collections import deque

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


# def dfs(grph, start):
#     stack = [start]
#     while stack:
#         node = stack.pop()
#         print(node)
#         for neigh in grph[node]:
#             stack.append(neigh)

# def dfs(grph, start):
#     print(start)
#     for neigh in grph[start]:
#         dfs(graph, neigh)

def bfs(g, s):
    queue = deque([s])
    while queue:
        node = queue.popleft()
        print(node)
        for neigh in g[node]:
            queue.append(neigh)


bfs(graph, 'a')
