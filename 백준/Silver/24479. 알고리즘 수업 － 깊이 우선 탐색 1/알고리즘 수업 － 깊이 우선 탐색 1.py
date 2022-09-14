from sys import stdin
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(graph, v, visited):
    global order
    visited[v] = order
    for i in graph[v]:
        if visited[i] == 0:
            order += 1
            dfs(graph, i, visited)

n, m, r = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
order = 1

for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(len(graph)):
    graph[i].sort()


dfs(graph, r, visited)

for i in range(1, len(visited)):
    print(visited[i])