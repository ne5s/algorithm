from sys import stdin

n = int(stdin.readline())
li = []
for i in range(n):
    li.append(int(stdin.readline()))
for i in sorted(li):
    print(i)