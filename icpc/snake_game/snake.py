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

    def explore_map(self, board, end, move):

        def bound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        rw, cl = self._position[1]
        queue = deque([(rw, cl, move)])
        pos = None

        for i in range(len(board)):
            for c in range(len(board[0])):
                queue.append((i, c, move))

        while queue:
            r, c, move = queue.popleft()
            pos = (r, c)

            if move == 0:
                return (r, c)

            # if curr player in trap do

            if pos in self._trap_set:
                return "game Over"

            pos = pos
            deltas = [(0, 1), (0, 2)]
            coin = self.flip_coin()

            for delta_r, delta_c in deltas:
                rrow = r + delta_r
                ccol = c + delta_c
                is_bound = bound(rrow, ccol)

                if is_bound:
                    print(board[rrow][ccol])
                pos = (rrow, ccol)
                #  head of snake

                if (is_bound and pos not in self._ladder_bottom
                        and board[rrow][ccol] != end):
                    queue.append(
                        (rrow, ccol, move - 1)) if coin == 1 else queue.append((rrow, c + 3, move - 1))

                elif (is_bound and pos and pos not in self._snake_head
                      and board[rrow][ccol] != end and pos == self._ladder_pos.get(pos)):
                    new_r_pos, new_c_pos = self._ladder_pos[(r, c)]
                    queue.append((new_r_pos, new_c_pos, move - 1))

                elif (rrow, ccol) in self._snake_head:
                    snake_tail_r, snake_tail_c = self._snake_head[(
                        rrow, ccol)]
                    queue.append((snake_tail_r, snake_tail_c, move - 1))

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

        return self.explore_map(board=board, end=end, move=move)


game = Game()

snakes = [Snake(head=78, tail=48), Snake(
    head=55, tail=22), Snake(head=85, tail=58)]

traps = [23, 45, 67]

ladders = [Ladder(bottom=2, top=30), Ladder(bottom=12, top=25)]

game = game.play(board_size=10, snakes=snakes,
                 ladders=ladders, traps=traps, move=10)

print(game)
