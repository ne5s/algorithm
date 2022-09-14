from sys import stdin

n, k = map(int, stdin.readline().split())
li = []
for i in range(n):
    li.append(int(stdin.readline()))
li.sort(reverse=True)
count = 0
for i in li:
    a, b = divmod(k, i)
    count += a
    k = b

print(count)