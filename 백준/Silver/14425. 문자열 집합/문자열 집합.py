from sys import stdin

n, m = map(int, stdin.readline().split())
a = set()
count = 0
for i in range(n):
    a.add(stdin.readline().rstrip())
for i in range(m):
    inp = stdin.readline().rstrip()
    if inp in a:
        count += 1
print(count)