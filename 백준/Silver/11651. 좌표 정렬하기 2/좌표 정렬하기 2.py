from sys import stdin

N = int(stdin.readline())
li = []
for i in range(N):
    x, y = map(int, stdin.readline().split())
    li.append((x,y))

for i in sorted(li, key= lambda x : (x[1], x[0])):
    x,y = i
    print(x, y)