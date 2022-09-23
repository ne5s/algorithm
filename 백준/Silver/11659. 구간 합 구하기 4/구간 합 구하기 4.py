from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
sum_list = [0]
total = 0
for i in range(n):
    total += arr[i]
    sum_list.append(total)

for _ in range(m):
    i, j = map(int, stdin.readline().split())
    print(sum_list[j] - sum_list[i-1])