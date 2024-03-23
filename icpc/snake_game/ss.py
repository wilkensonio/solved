import random


class SnakesAndLadders:
    def __init__(self, board_size, snakes, ladders, traps):
        self.board_size = board_size
        self.snakes = snakes
        self.ladders = ladders
        self.traps = traps
        self.players = [0] * len(traps)

    def flip_coin(self):
        return random.choice(["Head", "Tail"])

    def move_player(self, player_index):
        coin_result = self.flip_coin()
        if coin_result == "Head":
            self.players[player_index] += 2
        else:
            self.players[player_index] += 3

        if self.players[player_index] in self.snakes:
            self.players[player_index] = self.snakes[self.players[player_index]]
        elif self.players[player_index] in self.ladders:
            self.players[player_index] = self.ladders[self.players[player_index]]

        if self.players[player_index] in self.traps:
            # Player is trapped, game over for this player
            self.players[player_index] = -1

    def simulate_game(self, num_steps):
        player_positions_over_time = [[] for _ in range(len(self.players))]
        for step in range(num_steps):
            for i in range(len(self.players)):
                if self.players[i] != -1:  # Check if player is still in the game
                    self.move_player(i)
                player_positions_over_time[i].append(self.players[i])
                if self.players[i] == self.board_size:
                    return player_positions_over_time  # Game finished, return player positions
        return player_positions_over_time


# Example usage:
board_size = 100
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19,
          64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42,
           28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
traps = {8, 21, 40, 55, 69, 88}

game = SnakesAndLadders(board_size, snakes, ladders, traps)
player_positions = game.simulate_game(100)
print(player_positions)
