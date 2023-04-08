from sys import stdin


def grid_setup(matrix):
    # N X M grid
    n, m = (int)(matrix[0]), (int)(matrix[1])

    grid = []
    for row in matrix[2:]:
        grid.append([int(x) for x in row])

    return grid, n, m


def find_path(matrix):
    start = (0, 0)
    grid, n, m = grid_setup(matrix)
    end_y, end_x = (len(grid) - 1, len(grid[0]) - 1)

    visited = set([start])
    current_node = [(start, 0)]

    while current_node:
        node, num_moves = current_node.pop(0)

        max_jump = grid[node[0]][node[1]]

        directions = [(node[1] + max_jump, node[0]),
                      (node[1] - max_jump, node[0]),
                      (node[1], node[0] + max_jump),
                      (node[1], node[0] - max_jump)]

        for next_node_y, next_node_x in directions:
            if (0 <= next_node_y <= end_y
                and 0 <= next_node_x <= end_x
                and (next_node_y, next_node_x)
                    not in visited):

                visited.add((next_node_y, next_node_x))
                current_node.append(
                    ((next_node_y, next_node_x), num_moves + 1))

        if node == (n - 1, m - 1):
            return num_moves

    return -1


arr = []
for item in stdin:
    arr += item.split()

print(find_path(arr))
