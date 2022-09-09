from sys import stdin

n = int(stdin.readline())
li = list(map(int, stdin.readline().split()))
v = int(stdin.readline())

sum = 0
for i in li:
    if i == v:
        sum += 1
print(sum)