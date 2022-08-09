from sys import stdin
n = int(stdin.readline())
s = ""
for i in range(n):
    a, b = list(map(int, stdin.readline().split()))
    s += (str(a+b) + '\n')
print(s)