from sys import stdin

n = int(stdin.readline())
li = list(map(int, stdin.readline().split()))
li.sort()
print(li[0] * li[-1])



