from sys import stdin

N = int(stdin.readline())
li = []
for _ in range(N):
    li.append(list(map(int, stdin.readline().split())))
# print(li)
white = 0
blue = 0
def dq(arr, x_st, y_st, size):
    global white, blue
    flag = 0
    flag2 = 0
    if size == 1:
        if arr[x_st][y_st] == 0:
            white += 1
        else:
            blue += 1
        return
    check = li[x_st][y_st]
    for i in range(x_st, x_st+size):
        if flag2:
            break
        for j in range(y_st, y_st+size):
            if arr[i][j] != check:
                flag = 1
                dq(arr, x_st, y_st, size//2) # 좌 상
                dq(arr, x_st+size//2, y_st, size//2) # 좌 하
                dq(arr, x_st, y_st+size//2, size//2) # 우 상
                dq(arr, x_st+size//2, y_st+size//2, size//2) # 우 하
                flag2 = 1
                break
    if not flag:
        if check:
            blue += 1
        else:
            white += 1

dq(li, 0, 0, N)
print(str(white) + "\n" + str(blue))