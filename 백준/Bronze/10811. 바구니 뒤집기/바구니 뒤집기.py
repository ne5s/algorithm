from sys import stdin

def p(N, M):
    list = [0] * (N + 1)
    for i in range(0, N + 1):
        list[i] = i

    for _ in range(M):
        i, j = map(int, stdin.readline().split())
        cnt = 0
        for q in range(i, int((i + j)/2) + 1):
            temp = list[q]
            list[q] = list[j - cnt]
            list[j - cnt] = temp
            cnt += 1


    for i in range(1, N + 1):
        print(list[i], end=' ')

if __name__ == "__main__":
    N, M = map(int, stdin.readline().split())
    p(N, M)