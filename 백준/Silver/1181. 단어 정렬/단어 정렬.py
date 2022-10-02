from sys import stdin

N = int(stdin.readline())
li = set()
for i in range(N):
    s = stdin.readline().rstrip()
    li.add((len(s), s))
for _, st in sorted(li):
    print(st)