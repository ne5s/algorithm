class Solution {
    public int solution(int[][] board) {
        int len = board.length;
        int answer = len * len;

        // 위, 좌상단대각, 좌, 좌하단대각, 하단, 우하단대각, 우, 우상단대각
        int[] rx = {-1, -1, 0, 1, 1, 1, 0, -1};
        int[] ry = {0, -1, -1, -1, 0, 1, 1, 1};

        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                if (board[i][j] == 1) {
                    answer--;
                    board[i][j] = 3;
                    for (int k = 0; k < 8; k++) {
                        int nx = i + rx[k];
                        int ny = j + ry[k];
                        if (nx >= len || nx < 0 || ny >= len || ny < 0) {
                            continue;
                        }
                        if (board[nx][ny] == 0) {
                            board[nx][ny] = 4;
                            answer--;
                        }
                    }
                }
            }
        }
        return answer;
    }
}