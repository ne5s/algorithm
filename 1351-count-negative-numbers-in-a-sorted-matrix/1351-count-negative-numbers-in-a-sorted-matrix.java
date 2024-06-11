class Solution {
    public int countNegatives(int[][] grid) {
        int rowLen = grid.length;
        int columnLen = grid[0].length;
        int row = 0;
        int col = columnLen - 1;
        int negativeNumCount = 0;

        while (row < rowLen && col >= 0) {
            if (grid[row][col] < 0) {
                negativeNumCount += (rowLen - row);
                col--;
            } else {
                row++;
            }
        }
        return negativeNumCount;
    }
}

//  4  3  2 -1
//  3  2  1 -1
//  1  1 -1 -2
// -1 -1 -2 -3

// 3 2
// 1 0

//  3  2
// -3 -3
// -3 -3
// -3 -3