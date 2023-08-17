"""
closest carrot
Write a function, closest_carrot, that takes in a grid, a starting row, and a starting column.
In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots. The function should
return a number representing the length of the shortest path from the starting position to a carrot.
You may move up, down, left, or right, but cannot pass through walls (X). If there is no possible path
to a carrot, then return -1.
"""


def closest_carrot(grid, starting_row, starting_col):
    return breath_first_search(grid, starting_row, starting_col)


def breath_first_search(grid, start_r, start_c):
    visited = set((start_r, start_c))
    queue = [(start_r, start_c, 0)]

    while queue:
        row, col, distance = queue.pop(0)

        if grid[row][col] == 'C':
            return distance

        delta_positions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for delta_row, delta_col in delta_positions:
            neigh_row = row + delta_row
            neigh_col = col + delta_col

            row_inbound = 0 <= neigh_row < len(grid)
            col_inbound = 0 <= neigh_col < len(grid[0])

            visited_pos = (neigh_row, neigh_col)
            if (row_inbound and col_inbound and visited_pos not in visited
                    and grid[neigh_row][neigh_col] != 'X'
            ):
                queue.append((neigh_row, neigh_col, distance + 1))
                visited.add(visited_pos)

    return -1


grid = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['O', 'X', 'C', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['C', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 1, 2))
