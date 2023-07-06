import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<String> row = new HashSet<>();
        Set<String> col = new HashSet<>();
        Set<String> grid = new HashSet<>();

        for (int idx = 0; idx < 81; idx++) {
            int i = idx / 9;
            int j = idx % 9;

            if (board[i][j] == '.') {
                continue;
            }

            if (row.contains("" + i + board[i][j])
                    || col.contains("" + j + board[i][j])
                    || grid.contains("" + (i / 3) + (j / 3) + board[i][j])) {
                return false;
            }
            row.add("" + i + board[i][j]);
            col.add("" + j + board[i][j]);
            grid.add("" + (i / 3) + (j / 3) + board[i][j]);
        }
        return true;
    }
}