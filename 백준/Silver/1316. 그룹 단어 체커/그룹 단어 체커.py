from sys import stdin

N = int(stdin.readline())
sum = 0
for i in range(N):
    a = stdin.readline().rstrip()
    if list(a) == sorted(a, key=a.find):
        sum += 1
print(sum)

