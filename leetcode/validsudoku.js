function isValidSudoku(board) {
  const row = new Set();
  const col = new Set();
  const grid = new Set();

  for (let index = 0; index < 81; index++) {
    const i = Math.floor(index / 9);
    const j = index % 9;

    if (board[i][j] === '.') {
      continue;
    }

    if (
      grid.has(`${Math.floor(i / 3)}${Math.floor(j / 3)}${board[i][j]}`)
      || row.has(`${i}${board[i][j]}`)
      || col.has(`${j}${board[i][j]}`)
    ) {
      return false;
    }

    row.add(`${i}${board[i][j]}`);
    col.add(`${j}${board[i][j]}`);
    grid.add(`${Math.floor(i / 3)}${Math.floor(j / 3)}${board[i][j]}`);
  }

  return true;
}

board = [
    ["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

console.log(isValidSudoku(board))