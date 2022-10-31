from sys import stdin
from collections import deque

def bfs(start):
    global order
    visited[start] = order
    dq.append(start)
    while len(dq) != 0:
        node = dq.popleft()
        for adj in graph[node]:
            if not visited[adj]:
                order += 1
                visited[adj] = order
                dq.append(adj)


n, m, r = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
dq = deque()
visited = [0] * (n+1)
order = 1

for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(len(graph)):
    graph[i].sort()

bfs(r)

for i in range(1, len(visited)):
    print(visited[i])
    