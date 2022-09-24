from sys import stdin
import sys
sys.setrecursionlimit(10 ** 6)

#  (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
# nC2 여서 N×(N-1)/2 간선의 개수가 N^2에 근접하니까 인접행렬에 값이 다 채워질 수 있다
# 인접행렬 쓰는 것이 낫겠다

n, m = map(int, stdin.readline().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u][v] = graph[v][u] = 1

ans = 0
chk = [False] * (n+1)

def dfs(now):
    for nxt in range(1, n+1):
        if graph[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)

for i in range(1, n+1):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)