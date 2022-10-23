from sys import stdin

N, M, K = map(int, stdin.readline().split())
cnt = 0
if M >= K:
    cnt += K
    cnt += (N-M)
    # 4 3 2
    # o - 3, x - 1
    # o - 2, x - 2
else:
    cnt += M
    cnt += (N-K)
    # 10 2 8
    # o - 2, x - 8
    # o -8, x - 2
print(cnt)