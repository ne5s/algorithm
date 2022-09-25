from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
arr = []
for i in range(n):
    a = stdin.readline().rstrip()
    li = []
    for j in a:
        li.append(int(j))
    arr.append(li)

dx = [0, 1, 0 , -1]
dy = [1, 0, -1, 0]

def bfs(s_x,s_y):
    chk = [[False] * (m+1) for _ in range(n+1)]
    chk[s_x][s_y] = True
    dq = deque()
    dq.append((s_x, s_y))
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not arr[nx][ny]:
                continue
            if chk[nx][ny]:
                continue
            chk[nx][ny] = True
            arr[nx][ny] = arr[x][y] + 1
            dq.append((nx, ny))

    return arr[n-1][m-1]

print(bfs(0,0))