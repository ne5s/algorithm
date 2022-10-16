from sys import stdin

N, M = map(int, stdin.readline().split())
arr1 = [[] for _ in range(N)]
arr2 = [[] for _ in range(N)]

for i in range(N):
    a = list(map(int, stdin.readline().split()))
    for j in a:
        arr1[i].append(j)

for i in range(N):
    a = list(map(int, stdin.readline().split()))
    for j in a:
        arr2[i].append(j)

for i in range(N):
    for j in range(M):
        print(arr1[i][j] + arr2[i][j], end=' ')
    print()