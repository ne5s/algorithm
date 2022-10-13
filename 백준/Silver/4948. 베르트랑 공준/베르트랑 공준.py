import math
from sys import stdin

li = [True] * 246913
for i in range(2, int(math.sqrt(len(li)) + 1)):
    if li[i] == True:
        j = 2
        while i * j <= len(li):
            li[i * j] = False
            j += 1
while True:
    n = int(stdin.readline())
    cnt = 0
    if n == 0:
        break
    for q in range(n+1, 2*n+1):
        if li[q]:
            cnt += 1
    print(cnt)
