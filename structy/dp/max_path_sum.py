"""

max path sum
Write a function, max_path_sum, that takes in a grid as an argument.
The function should return the maximum sum possible by traveling a path from the top-left corner to the bottom-right corner.
You may only travel through the grid by moving down or right.

You can assume that all numbers are non-negative."""

import random


def max_path_sum(grid):
    return _max_path_sum(grid, 0, 0, {})


def _max_path_sum(grid, r, c, dp):
    pos = (r, c)
    if pos in dp:
        return dp[pos]
    if r == len(grid) or c == len(grid[0]):
        return float('-inf')
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return grid[r][c]

    down = _max_path_sum(grid, r + 1, c, dp)
    right = _max_path_sum(grid, r, c + 1, dp)
    dp[pos] = max(down, right) + grid[r][c]
    return dp[pos]


grid = [
    [1, 3, 12],
    [5, 1, 1],
    [3, 6, 1],
]
print(max_path_sum(grid))  # -> 18
grid = [
    [1, 2, 8, 1],
    [3, 1, 12, 10],
    [4, 0, 6, 3],
]
print(max_path_sum(grid))  # -> 36
grid = [
    [1, 2, 8, 1],
    [3, 10, 12, 10],
    [4, 0, 6, 3],
]
print(max_path_sum(grid))  # -> 39


grid = [[random.randint(0, 10) for _ in range(100)] for _ in range(100)]

print(max_path_sum(grid))
