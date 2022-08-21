from sys import stdin

n = int(stdin.readline())
sol = list(map(int, stdin.readline().split()))
sol = set(sol)
m = int(stdin.readline())
ipt = list(map(int, stdin.readline().split()))
print(" ".join(map(lambda x: "1" if x in sol else "0", ipt)))
