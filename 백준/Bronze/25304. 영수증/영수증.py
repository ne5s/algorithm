from sys import stdin
sum = int(stdin.readline())
num = int(stdin.readline())
cal_sum = 0
for i in range(num):
    a, b = list(map(int, stdin.readline().split()))
    cal_sum += (a * b)
print("Yes" if sum == cal_sum else "No")