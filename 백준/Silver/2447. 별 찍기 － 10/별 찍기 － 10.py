from sys import stdin

def recursive(x, y, n, li):
    if n == 3:
        li[x+1][y+1] = ' '
    else:
        temp = n // 3
        # 빈 공간으로 바꿔주기
        for i in range(x+temp, x + temp*2):
            for j in range(y+temp, y + temp*2):
                li[i][j] = ' '
        # 분할정복
        for i in range(0, n, temp):
            for j in range(0, n, temp):
                recursive(x+i, y+j, temp, li)

n = int(stdin.readline().rstrip())
li = [["*" for _ in range(n)] for _ in range(n)]
recursive(0, 0, n, li)
for i in range(n):
    for j in range(n):
        print(li[i][j], end='')
    print()