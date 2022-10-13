from sys import stdin

N = int(stdin.readline())
li = []
for _ in range(N):
    age, name = stdin.readline().split()
    li.append([int(age), name])
li.sort(key=lambda x: x[0])
for i in li:
    print(i[0], i[1])