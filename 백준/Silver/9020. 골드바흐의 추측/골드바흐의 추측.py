# 내 코드
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

answer = ''
for _ in range(T):
    N = int(input())
    if N == 4:
        answer += "2 2\n"
        continue
    harf_N = N // 2
    if not harf_N % 2:
        harf_N += 1
    for i in range(harf_N, N, 2):
        if li[i] and li[N - i]:
            answer += "{} {}".format(N - i, i) + "\n"
            break
print(answer, end="")