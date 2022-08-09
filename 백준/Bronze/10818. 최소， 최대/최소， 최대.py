from sys import stdin

a = int(stdin.readline())

li = list(map(int, stdin.readline().split()))
li.sort()
print(li[0], li[-1])
