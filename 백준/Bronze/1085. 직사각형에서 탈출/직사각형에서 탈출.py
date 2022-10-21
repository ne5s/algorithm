from sys import stdin

x, y, w, h = map(int, stdin.readline().split())
print(min(x-0, y-0, w-x, h-y))