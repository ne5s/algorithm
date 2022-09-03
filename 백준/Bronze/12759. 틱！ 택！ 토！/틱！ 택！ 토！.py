from sys import stdin

def check(x):
    # 행단위 확인
    for i in range(len(li)):
        for j in range(len(li[0])):
            if li[i][j] != x:
                break
            if j == (len(li[0]) - 1):
                return x
    # 열단위 확인
    for i in range(len(li[0])):
        for j in range(len(li)):
            if li[j][i] != x:
                break
            if j == (len(li) - 1):
                return x
    # 좌상우하 대각선 확인
    for i in range(len(li)):
        if li[i][i] != x:
            break
        if i == (len(li) - 1):
            return x
    # 우상좌하 대각선 확인
    for i in range(len(li)):
        if li[i][2 - i] != x:
            break
        if i == (len(li) - 1):
            return x
    return 0

n = int(stdin.readline()) # 2 또는 1
li = [[0]*3 for i in range(3)]
checksum = False
for i in range(9):
    x, y = map(int, stdin.readline().split())
    x -= 1; y -= 1;
    # 첫 순서가 2라면
    if n == 2:
        li[x][y] = 2
        # 여기서부터 게임 종료인 지 확인
        if not checksum:
            winner = check(n)
            if winner != 0:
                checksum = True
        n = 1
    else:
        li[x][y] = 1
        # 여기서부터 게임 종료인 지 확인
        if not checksum:
            winner = check(n)
            if winner != 0:
                checksum = True
        n = 2

print(winner)