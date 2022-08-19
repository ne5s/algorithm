from sys import stdin
from collections import deque

n = int(stdin.readline())
dq = deque()
for i in range(n):
    temp = stdin.readline()
    cmd = temp.split()[0]
    if cmd == 'push':
        dq.append(temp.split()[1])
    elif cmd == 'pop':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif cmd == 'size':
        print(len(dq))
    elif cmd == 'empty':
        print(1) if len(dq) == 0 else print(0)
    elif cmd == 'front':
        print(-1) if len(dq) == 0 else print(dq[0])
    elif cmd == 'back':
        print(-1) if len(dq) == 0 else print(dq[-1])