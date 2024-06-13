class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        int[][] graph = new int[n + 1][n + 1];

        // 승패기록 저장
        for (int[] result : results) {
            graph[result[0]][result[1]] = 1; // result 0이 1을 이김
            graph[result[1]][result[0]] = -1; // result 1이 0을 이김
        }

        // 플로이드 워셜 알고리즘으로 모든 쌍의 승패 파악
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (graph[i][k] == 1 && graph[k][j] == 1) {
                        graph[i][j] = 1; // i가 k를 이기고 k가 j를 이기면 i가 j를 이김
                        graph[j][i] = -1;// j가 i에게 짐
                    }
                }
            }
        }

        // 순위 결정 가능한 선수 수 계산
        for (int i= 1; i <= n; i++) {
            int count = 0;
            for (int j = 1; j <= n; j++) {
                if (i != j && (graph[i][j] != 0 || graph[j][i] != 0)) {
                    count++;
                }
            }
            // 행렬의 0은 이미 시작부에서 제외됐고
            // 1~n 까지 봤을 때 자기 자신을 제외한 n-1개가 모두 결정이 된다면
            if (count == n - 1) {
                answer++;
            }
        }
        return answer;
    }
}

// 1 - 1/0
// 2 - 0/3
// 3 - 1/1
// 4 - 2/0
// 5 - 0/1

// 0 0 0 0 0 0
// 0 0
// 0 -1 0 -1-1 1
// 0   1 0 -1
// 0   1 1 0
// 0  -1     0