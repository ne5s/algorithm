from sys import stdin
from collections import deque

n = int(stdin.readline())
dq = deque()
for i in range(1, n+1):
    dq.append(i)
while len(dq) > 1:
    dq.popleft()
    two = dq.popleft()
    dq.append(two)

print(dq[0])
