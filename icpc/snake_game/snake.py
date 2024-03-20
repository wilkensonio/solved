import random
from dataclasses import dataclass, field
from random import randint
import pprint


@dataclass
class Snake:
    board_dim: int = None
    coin_flip: int = None
    trap_list: list[int] = field(default_factory=list)
    ladder_list: list[tuple[int, int]] = field(default_factory=list)

    def create_board(self, dim):
        board = [[str(i + 1 + j * dim) for i in range(dim)]
                 for j in range(dim)]
        return board

    def set_trap(self, tile: int):
        self.trap_list.append(tile)

    def set_ladder(self, latter_head: int, ladder_tail: int):
        trap = (latter_head, ladder_tail)
        self.ladder_list.append(trap)

    def flip_coin(self):
        """if flip is one then head else tail"""
        self.coin_flip = randint(1, 2)

    def move(self):
        pass

    def play(self, board: int, coin_head: int, coin_teal: int, lastt):
        return self.coin_head


game = Snake()
# print(game.play())
pprint.pprint(game.create_board(10))

# Generate a random integer between 1 and 10
random_number = random.randint(1, 2)
print(random_number)
