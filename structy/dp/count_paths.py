"""
count paths
Write a function, count_paths, that takes in a grid as an argument.
In the grid, 'X' represents walls and 'O' represents open spaces.
You may only move down or to the right and cannot pass through walls.
The function should return the number of ways possible to travel from
the top-left corner of the grid to the bottom-right corner.
"""


def count_paths(grid):
    return _count_paths(grid, 0, 0, {})


def _count_paths(grid, r, c, dp):
    pos = (r, c)
    if pos in dp:
        return dp[pos]
    if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
        return 0
    if r == len(grid) - 1 and len(grid[0]) - 1 == c:
        return 1

    down = _count_paths(grid, r + 1, c, dp)
    right = _count_paths(grid, r, c + 1, dp)
    dp[pos] = down + right
    return dp[pos]


grid = [
    ["O", "O"],
    ["O", "O"],
]
print(count_paths(grid)) # -> 2
grid = [
    ["O", "O", "X"],
    ["O", "O", "O"],
    ["O", "O", "O"],
]
print(count_paths(grid)) # -> 5
grid = [
    ["O", "O", "O"],
    ["O", "O", "X"],
    ["O", "O", "O"],
]
print(count_paths(grid)) # -> 3