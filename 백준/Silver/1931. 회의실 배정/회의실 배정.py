from sys import stdin

N = int(stdin.readline())
li = []
for _ in range(N):
    start, end = map(int, stdin.readline().split())
    li.append([start, end])

li.sort(key=lambda x: (x[1], x[0]))

# print(li)
confer = 1
last = li[0][1]
for i in range(1, N):
    if li[i][0] >= last:
        confer += 1
        last = li[i][1]
print(confer)
