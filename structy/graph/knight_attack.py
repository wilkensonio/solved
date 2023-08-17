"""
knight attack
A knight and a pawn are on a chess board. Can you figure out the minimum number of moves
required for the knight to travel to the same position of the pawn? On a single move, the knight
can move in an "L" shape; two spaces in any direction, then one space in a perpendicular direction.
This means that on a single move, a knight has eight possible positions it can move to.

Write a function, knight_attack, that takes in 5 arguments:

n, kr, kc, pr, pc

n = the length of the chess board
kr = the starting row of the knight
kc = the starting column of the knight
pr = the row of the pawn
pc = the column of the pawn
The function should return a number representing the minimum number of moves
required for the knight to land ontop of the pawn. The knight cannot move out-of-bounds of the board.
You can assume that rows and columns are 0-indexed. This means that if n = 8, there are 8 rows and 8
columns numbered 0 to 7. If it is not possible for the knight to attack the pawn, then return None.

"""


def knight_attack(n, kr, kc, pr, pc):
    queue = [(kr, kc, 0)]
    visited = {kr, kc}

    while queue:
        r, c, step = queue.pop(0)
        if (r, c) == (pr, pc):
            return step

        neighbors: list[tuple[int, int]] = neighboring_pos(n, r, c)

        for neigh_row, neigh_col in neighbors:
            if (neigh_row, neigh_col) not in visited:
                queue.append((neigh_row, neigh_col, step + 1))
                visited.add((neigh_row, neigh_col))

    return None


def neighboring_pos(n, r, c) -> list[tuple[int, int]]:
    positions = [
        (r + 2, c + 1),
        (r - 2, c + 1),
        (r + 2, c - 1),
        (r - 2, c - 1),
        (r + 1, c + 2),
        (r + 1, c - 2),
        (r - 1, c + 2),
        (r - 1, c - 2)
    ]

    valid: list[tuple[int, int]] = []
    for pos in positions:
        if 0 <= r < n and 0 <= c < n:
            valid.append(pos)

    return valid


print(knight_attack(8, 1, 1, 2, 2))  # -> 2
print(knight_attack(8, 1, 1, 2, 3))  # ->11
print(knight_attack(100, 21, 10, 0, 0))  # -> 11
