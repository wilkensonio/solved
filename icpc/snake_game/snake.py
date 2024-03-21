import random
from dataclasses import dataclass, field
from collections import deque
from random import randint
import pprint


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
    _coin_flip: int = None
    _trap_set: set[tuple[int, int]] = field(default_factory=set)
    _ladder_bottom: set[tuple[int, int]] = field(default_factory=set)
    _position: dict[int, tuple[int, int]] = field(default_factory=dict)

    _ladder_pos: dict[tuple[int, int], tuple[int, int]
                      ] = field(default_factory=dict)

    _snake_head: dict[tuple[int, int],
                      tuple[int, int]] = field(default_factory=dict)

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

    def set_trap(self, tile: int):
        if tile in self._position:
            self._trap_set.add(self._position[tile])

    def flip_coin(self):
        """if flip is one then head else tail"""
        self._coin_flip = randint(1, 2)
        return self._coin_flip

    def bound(self, board, r, c):
        return 0 <= r < len(board) and 0 <= c < len(board[0])

    def explore_map(self, board, r, c, end, move):
        if not self.bound(board, r, c):
            return None
        if (r, c) in self._trap_set:
            return "Game Over"

        if board[r][c] == end:
            return (r, c)

        if move == 0:
            return (r, c)

        coin_val = self.flip_coin()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if coin_val == 1:
                    self.explore_map(board, i, j + 1, end, move - 1)
                    self.explore_map(board, i, j + 2, end, move - 2)
                else:
                    self.explore_map(board, i, j + 3, end, move - 3)

    def play(self, board_size: int, snakes: list, ladders: list, traps: list, move: int):

        board = self.create_board(board_size)
        end = board_size * board_size

        for trap in traps:
            self.set_trap(trap)

        for snake in snakes:
            self._snake_head[snake.head] = self._position[snake.tail]

        for ladder in ladders:
            self._ladder_pos[self._position[ladder.bottom]
                             ] = self._position[ladder.top]

        row, col = self._position[1]
        return self.explore_map(board, row, col, end, move)


game = Game()

snakes = [Snake(head=78, tail=48), Snake(
    head=55, tail=22), Snake(head=85, tail=58)]

traps = [23, 45, 67]

ladders = [Ladder(bottom=2, top=30), Ladder(bottom=12, top=25)]

game = game.play(board_size=10, snakes=snakes,
                 ladders=ladders, traps=traps, move=10)

print(game)
