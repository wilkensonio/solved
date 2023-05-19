from sys import stdin


def grid_setup(matrix):
    print(matrix)
    n, m = (int)(matrix[0]), (int)(matrix[1])

    grid = []
    for row in matrix[2:]:
        grid.append([int(x) for x in row])
    return grid, n, m


def find_path(matrix):
    start = (0, 0)
    grid, n, m = grid_setup(matrix)
    len_y, len_x = (len(grid) - 1, len(grid[0]) - 1)

    visited = set([start])
    current_node = [(start, 0)]

    while current_node:
        (y, x), num_moves = current_node.pop(0)

        max_jump = grid[y][x]

        directions = [(y + max_jump, x),
                      (y - max_jump, x),
                      (y, x + max_jump),
                      (y, x - max_jump)]

        for next_y, next_x in directions:
            if (0 <= next_y <= len_y
                and 0 <= next_x <= len_x
                and (next_y, next_x)
                    not in visited):
                visited.add((next_y, next_x))
                current_node.append(
                    ((next_y, next_x), num_moves + 1))

        if (y, x) == (n - 1, m - 1):
            return num_moves

    return -1


arr = []
for item in stdin:
    arr += item.split()

print(find_path(arr))
