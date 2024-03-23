from dataclasses import dataclass, field
import random


@dataclass
class Snake:
    head: int
    tail: int


@dataclass
class Ladder:
    bottom: int
    top: int


@dataclass
class Game:
    _coin_flip: str = None
    _snake_head: dict[tuple[int, int],
                      tuple[int, int]] = field(default_factory=dict)

    _ladder_pos: dict[tuple[int, int], tuple[int, int]
                      ] = field(default_factory=dict)

    _trap_set: set[tuple[int, int]] = field(default_factory=set)
    _position: dict[int, tuple[int, int]] = field(default_factory=dict)

    def create_board(self, dim: int):
        number = 1
        board = [[0] * dim for _ in range(dim)]
        for i in range(dim-1, -1, -1):
            for j in range(dim):
                board[i][j] = number
                self._position[number] = (i, j)
                self._position[(i, j)] = number
                number += 1
        return board

    def _set_trap(self, tile: int):
        if tile in self._position:
            self._trap_set.add(self._position[tile])

    def flip_coin(self):
        """if flip is one then head else tail"""
        self._coin_flip = random.choice(["head", "tail"])
        return self._coin_flip

    def bound(self, board, r, c):
        return 0 <= r < len(board) and 0 <= c < len(board[0])

    def explore_map(self, board, row, col, end, move):

        r, c = self._ladder_pos.get((row, col)) if (
            row, col) in self._ladder_pos else (row, col)

        if not self.bound(board, r, c):
            return ""

        if (r, c) in self._trap_set:
            return f"position {self._position[(r, c)]} Game Over"

        if board[r][c] == end:
            return f"position {self._position[(r, c)]} WIN end of game"

        if move <= 0:
            return f"position {self._position[(r, c)]} no more moves"

        coin_val: str = self.flip_coin()

        if coin_val == 'head':
            return self.explore_map(board, r, c + 2, end, move - 2)
        else:
            return self.explore_map(board, r, c + 3, end, move - 3)

    def play(self, board_size: int, snakes: list, ladders: list, traps: list, move: int):

        board = self.create_board(board_size)
        end = board_size * board_size
        final = ""

        for trap in traps:
            self._set_trap(trap)

        for snake in snakes:
            self._snake_head[snake.head] = self._position[snake.tail]

        for ladder in ladders:
            self._ladder_pos[self._position[ladder.bottom]
                             ] = self._position[ladder.top]

        for i in range(len(board) - 1, -1, -1):
            for j in range(len(board[0])):
                res = self.explore_map(board, i, j, end, move)
                if "no more moves" in res:
                    return res
                if "Game Over" in res:
                    return "Game Over"
                elif res:
                    final = res

        return final


game = Game()

traps = [2, 3]
# traps = []

snakes = [Snake(head=78, tail=48), Snake(
    head=55, tail=22), Snake(head=85, tail=58)]

ladders = [Ladder(bottom=2, top=30), Ladder(
    bottom=12, top=25), Ladder(bottom=3, top=25), Ladder(bottom=1, top=26)]

game = game.play(board_size=10, snakes=snakes,
                 ladders=ladders, traps=traps, move=7)

print(game)
