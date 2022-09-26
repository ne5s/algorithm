from sys import stdin

n, m = map(int, stdin.readline().split())
visited = [False] * n # 탐사 여부 check
res = [] # 출력 내용

def dfs(depth, n, m):
    if depth == m: # 탈출 조건
        print(' '.join(map(str, res))) # list를 str으로 합쳐 출력
        return
    for i in range(n): # 탐사 check 하면서
        if not visited[i]: # 탐사 안했다면
            visited[i] = True # 탐사 시작(중복 제거)
            res.append(i+1) # 탐사 내용
            dfs(depth+1, n, m) # 깊이 우선 탐색
            visited[i] = False # 깊이 탐사 완료
            res.pop() # 탐사 내용 제거


dfs(0, n, m)