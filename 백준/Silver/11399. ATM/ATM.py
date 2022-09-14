from sys import stdin

n = int(stdin.readline())
li = list(map(int, stdin.readline().split()))
li.sort()
sum = 0
for i in range(len(li)):
    mid = 0
    for j in range(i+1):
        mid += li[j]
    sum += mid
print(sum)