"""
best bridge
Write a function, best_bridge, that takes in a grid as an argument.
The grid contains water (W) and land (L). There are exactly two islands in the grid.
An island is a vertically or horizontally connected region of land.
Return the minimum length bridge needed to connect the two islands. A bridge does not need to form a straight line.
"""


def best_bridge(grid):
    main_island = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            island = explore(grid, r, c, set())
            if len(island) > 0:
                main_island = island
                break

    visited = set(main_island)
    queue = []
    for r, c in main_island:
        queue.append((r, c, 0))

    while queue:
        r, c, distance = queue.pop(0)
        if grid[r][c] == 'L' and (r, c) not in main_island:
            return distance - 1

        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for delta_row, delta_col in deltas:
            neighbor_r = r + delta_row
            neighbor_c = c + delta_col
            neighbor_pos = (neighbor_r, neighbor_c)

            if is_inbound(grid, neighbor_r, neighbor_c) and neighbor_pos not in visited:
                queue.append((neighbor_r, neighbor_c, distance + 1))
                visited.add(neighbor_pos)


def explore(grid, row, col, visited):
    if not is_inbound(grid, row, col) or grid[row][col] == 'W':
        return visited

    pos = (row, col)

    if pos in visited:
        return visited

    visited.add(pos)

    explore(grid, row - 1, col, visited)
    explore(grid, row + 1, col, visited)
    explore(grid, row, col - 1, visited)
    explore(grid, row, col + 1, visited)

    return visited


def is_inbound(grid, r, c):
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])
    return row_inbounds and col_inbounds


grid = [
    ["W", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "L"],
    ["L", "L", "L", "W", "L"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]

print(best_bridge(grid))  # -> 1


 
