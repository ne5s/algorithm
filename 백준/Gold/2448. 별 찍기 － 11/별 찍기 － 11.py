from sys import stdin

n = int(stdin.readline().rstrip())
tri = ["  *  ", " * * ", "*****"]
n = n // 3

def triangle(n):
    L = len(tri)
    for i in range(L):
        # 주어진 모양 복사해서 아래쪽에 두개의 모양 더 만들기
        tri.append(tri[i] + " " + tri[i])
        # 주어진 모양의 여백 만들기
        tri[i] = " " * L + tri[i] + " " * L

    return tri

cnt = 0
while n > 1:
    n = n // 2
    cnt += 1

for i in range(cnt):
    triangle(tri)

for t in tri:
    print(t)