let productExceptSelf = function (nums) {
    let len = nums.length;
    let result = new Array(len).fill(1);
    let preI = 1;
    let postI = 1;
    let i = 0;

    while (len > i) {
        result[i] *= preI;
        preI *= nums[i];
        result[len - i - 1] *= postI;
        postI *= nums[len - i - 1];
        i++;
    }
    return result;
}
//console.log(productExceptSelf([1, 2, 3, 4]));

let isValidSudoku = function(board) {
    const row = Array.from({ length: 9 }, () => new Set());
    const col = Array.from({ length: 9 }, () => new Set());
    const grid = Array.from({ length: 9 }, () => new Set());

    for (let r = 0; r < board.length ; r++) {
      for (let c = 0; c < board.length; c++) {
        const cellValue = board[r][c];
        if (cellValue === '.') {
          continue;
        }

        if (
          row[r].has(cellValue) ||
          col[c].has(cellValue) ||
          grid[Math.floor(r / 3) * 3 + Math.floor(c / 3)].has(cellValue)
        ) {
          return false;
        }

        row[r].add(cellValue);
        col[c].add(cellValue);
        grid[Math.floor(r / 3) * 3 + Math.floor(c / 3)].add(cellValue);
      }
    }

    return true;
  }
board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


console.log(isValidSudoku(board))