import java.util.LinkedList;
import java.util.Queue;

class Solution {
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    
    public int solution(int[][] maps) {
        int answer = -1;


        int result = bfs(0, 0, maps);
        return result == 1 ? answer : result;
    }

    public int bfs(int x, int y, int[][] maps) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});
        int n = maps.length;
        int m = maps[0].length;

        while (!queue.isEmpty()) {
            int[] pollOne = queue.poll();
            int nowX = pollOne[0];
            int nowY = pollOne[1];

            for (int i = 0; i < 4; i++) {
                int newX = nowX + dx[i];
                int newY = nowY + dy[i];

                if (newX < 0 || newY < 0 || newX >= n || newY >= m) {
                    continue;
                }
                if (maps[newX][newY] == 0) continue;

                if (maps[newX][newY] == 1) {
                    maps[newX][newY] = maps[nowX][nowY] + 1;
                    queue.add(new int[]{newX, newY});
                }
            }

        }
        return maps[n - 1][m - 1];
    }
}