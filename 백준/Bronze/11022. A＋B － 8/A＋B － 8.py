from sys import stdin
n = int(stdin.readline())
for i in range(n):
    a, b = list(map(int, stdin.readline().split()))
    print(f'Case #{i+1}: {a} + {b} = {a+b}')