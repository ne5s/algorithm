from sys import stdin

n, m = map(int, stdin.readline().split())
a = set(list(map(int, stdin.readline().split())))
b= set(list(map(int, stdin.readline().split())))

print(len(a-b)+len(b-a))