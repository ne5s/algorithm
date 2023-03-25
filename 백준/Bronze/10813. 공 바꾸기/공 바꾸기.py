from sys import stdin

def p(N, M):
    list = [0] * N
    for i in range(0, N):
        list[i] = i + 1

    for _ in range(M):
        i, j = map(int, stdin.readline().split())
        temp = list[i - 1]
        list[i - 1] = list[j - 1]
        list[j - 1] = temp

    for i in range(N):
        print(list[i], end=' ')

if __name__ == "__main__":
    N, M = map(int, stdin.readline().split())
    p(N, M)