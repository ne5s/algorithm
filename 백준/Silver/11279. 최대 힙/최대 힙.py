# max heap
from sys import stdin
import heapq

N = int(stdin.readline())
pq = []
for _ in range(N):
    a = int(stdin.readline())
    if a == 0 and len(pq) == 0:
        print(0)
    elif a == 0:
        print(-heapq.heappop(pq))
    else:
        heapq.heappush(pq, -a)
