from sys import stdin
n = int(stdin.readline())
li = []
for i in range(n):
    w, h = map(int, stdin.readline().split())
    li.append((w, h))

for i in li:
    rank = 1
    for j in li:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')