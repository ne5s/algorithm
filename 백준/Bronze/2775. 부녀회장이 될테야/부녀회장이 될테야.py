from sys import stdin

T = int(stdin.readline())
dp = [[0] * 15 for _ in range(15)]
# 0층 채우기
for i in range(len(dp[0])):
    dp[0][i] = i

# 나머지 층 채우기(dp)
for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        dp[i][j] = sum(dp[i-1][1:j+1])

for _ in range(T):
    k = int(stdin.readline())
    n = int(stdin.readline())
    print(dp[k][n])