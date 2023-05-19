import sys


def cave_exploration(tunnels):
    graph, n, m = tunnels  # Junction,
    print(graph, n, m)


def parse_input():
    tunnels = []
    for pairs in sys.stdin:
        tunnels.append(pairs.split())

    n, m = map(int, tunnels[0])  # N Junctions , M tunnels

    graph = {}

    for i in range(len(tunnels[1:])):
        u, v = map(int, tunnels[i + 1])

        if u not in graph:
            graph[u] = [v]
        else:
            graph[u].append(v)

        if v not in graph:
            graph[v] = [u]
        else:
            graph[v].append(u)

    return graph, n, m


cave_exploration(parse_input())
