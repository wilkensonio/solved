import collections as cd

grid_b = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


def valid_sudoku(board):
	row = cd.defaultdict(set)
	col = cd.defaultdict(set)
	grid = cd.defaultdict(set)  # key = (r // 3, c // 3)
	
	for r in range(len(board)):
		for c in range(len(board)):
			if board[r][c] == '.':
				continue
			if (
				board[r][c] in row[r]
				or board[r][c] in col[c]
				or board[r][c] in grid[(r // 3, c // 3)]
			):
				return False
			row[r].add(board[r][c])
			col[c].add(board[r][c])
			grid[(r // 3, c // 3)].add(board[r][c])
	
	return True


# print(valid_sudoku(grid_b))
def isPalindrome(s: str) -> bool:
	i, j = 0, len(s) - 1
	
	while i < j:
		while i < j and not alpha_num(s[i]):
			i += 1
		while j > i and not alpha_num(s[j]):
			j -= 1
		if s[i].lower() != s[j].lower():
			return False
		i, j = i + 1, j + 1
	return True


def alpha_num(char):
	return (
		ord('A') <= ord(char) <= ord('Z')
		or ord('a') <= ord(char) <= ord('z')
		or ord('0') <= ord(char) <= ord('9')
	)


print(isPalindrome("0P"))
print(alpha_num('-'))
