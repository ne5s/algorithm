from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    H, W, N = map(int, stdin.readline().split())
    f = 0
    ho = 0
    if N % H == 0:
        f = H * 100
        ho = N // H
    else:
        f = (N % H) * 100
        ho = 1 + N // H
    print(f+ho)