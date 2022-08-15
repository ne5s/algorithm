from sys import stdin

n, k = list(map(int, stdin.readline().split()))
li = sorted(list(map(int, stdin.readline().split())), reverse=True)
print(li[k-1])