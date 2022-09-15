from sys import stdin
from collections import deque
n = int(stdin.readline())
q = deque()
for i in range(n):
    a = stdin.readline().split()
    if len(a) == 2:
        q.append(a[1])
        continue
    if a[0] == 'front':
        print(-1 if len(q) == 0 else q[0])
    elif a[0] == 'back':
        print(-1 if len(q) == 0 else q[-1])
    elif a[0] == 'size':
        print(len(q))
    elif a[0] == 'empty':
        print(1 if len(q) == 0 else 0)
    elif a[0] == 'pop':
        print(-1 if len(q) == 0 else q.popleft())