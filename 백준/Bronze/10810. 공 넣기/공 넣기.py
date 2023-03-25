from sys import stdin

def p(N, M):
    list = [0] * N
    for _ in range(M):
        i, j, k = map(int, stdin.readline().split())
        for q in range(i-1, j):
            list[q] = k
    for i in range(len(list)):
        print(list[i], end=' ')

if __name__ == "__main__":
    N, M = map(int, stdin.readline().split())
    p(N, M)