from sys import stdin
import math

T = int(stdin.readline())
n = 10000
li = [True for _ in range(n+1)]
for i in range(2, int(math.sqrt(len(li))) + 1):
    if li[i]:
        j = 2
        while i * j <= n:
            li[i * j] = False
            j += 1

for _ in range(T):
    n = int(stdin.readline())
    li2 = []
    for q in range(2, len(li)):
        if li[q]:
            n2 = n - q
            if li[n2]:
                li2.append([min(q, n2), max(q, n2), abs(q-n2)])
    li2.sort(key=lambda x:x[2])
    print(li2[0][0], li2[0][1])
