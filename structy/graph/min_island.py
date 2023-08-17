"""
minimum island
Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

You may assume that the grid contains at least one island.
"""


def minimum_island(grid):
    visited = [[0] * len(grid) for _ in range(len(grid))]
    min_island = 10 * 99
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            size = visiting(grid, r, c, visited)
            if size > 0:
                min_island = min(min_island, size)

    return min_island


def visiting(grid, r, c, visited):
    r_bound = 0 <= r < len(grid)
    c_bound = 0 <= c < len(grid[0])

    if not r_bound or not c_bound:
        return 0

    if grid[r][c] == 'W':
        return 0

    if visited[r][c] == 1:
        return 0

    visited[r][c] = 1

    size = 1
    size += visiting(grid, r - 1, c, visited)
    size += visiting(grid, r + 1, c, visited)
    size += visiting(grid, r, c - 1, visited)
    size += visiting(grid, r, c + 1, visited)

    return size


matrix = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_island(matrix))


def minimum_island(grid):
    visited = set()
    min_size = float("inf")
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore_size(grid, r, c, visited)
            if size > 0 and size < min_size:
                min_size = size
    return min_size


def explore_size(grid, r, c, visited):
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])
    if not row_inbounds or not col_inbounds:
        return 0

    if grid[r][c] == 'W':
        return 0

    pos = (r, c)
    if pos in visited:
        return 0
    visited.add(pos)

    size = 1
    size += explore_size(grid, r - 1, c, visited)
    size += explore_size(grid, r + 1, c, visited)
    size += explore_size(grid, r, c - 1, visited)
    size += explore_size(grid, r, c + 1, visited)
    return size
