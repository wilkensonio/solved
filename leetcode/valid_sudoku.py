import collections

_board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]],


def valid_sudoku(board: list[[str]]):
	valid_row = collections.defaultdict(set)
	valid_col = collections.defaultdict(set)
	valid_grid = collections.defaultdict(set)  # sub-grid

	for row in range(len(board)):
		for col in range(len(board)):
			if board[row][col] == '.':
				continue
			if (board[row][col] in valid_row[row]
					or board[row][col] in valid_col[col]
					or board[row][col] in valid_grid[(row // 3, col // 3)]):
				return False
			valid_row[row].add(board[row][col])
			valid_col[col].add(board[row][col])
			valid_grid[(row // 3, col // 3)].add(board[row][col])
	# print(dict(valid_row))
	# print(valid_col)
	print(valid_grid)
	return True


print(valid_sudoku(_board))
