from sys import stdin

N = int(stdin.readline())
li = dict()

nums = list(map(int, stdin.readline().split()))
# print(nums)
for i in nums:
    if i in li:
        li[i] += 1
    else:
        li[i] = 1
M = int(stdin.readline())
numss = list(map(int, stdin.readline().split()))
for j in numss:
    if j in li:
        print(li[j], end=' ')
    else:
        print(0, end=' ')