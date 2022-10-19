from sys import stdin
import heapq

N = int(stdin.readline())
hq = []
for _ in range(N):
    i = int(stdin.readline())
    if i == 0 and len(hq) == 0:
        print(0)
    elif i == 0:
        print(heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq, (abs(i), i))