from sys import stdin

a,b,c = list(map(int, stdin.readline().split()))
result = 0
if b >= c:
    result = -1
else:
    result = int(a / (c-b)) + 1

print(result)
