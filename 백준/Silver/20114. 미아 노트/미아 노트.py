from sys import stdin
n, h, w = map(int, stdin.readline().split())
li = []
ans = ''
# n : 원래 문자열 길이, h : 세로 중복개수, w : 가로 중복 개수
for _ in range(h):
    li.append(stdin.readline().rstrip())

def find(x):
    global ans
    for i in range(x * w, (x + 1) * w):
        for j in range(h):
            if li[j][i] != '?':
                ans += li[j][i]
                return
    ans += '?'
    return

for i in range(n):
    find(i)
print(ans)