from sys import stdin

k, d, a = map(int, stdin.readline().rstrip().split('/'))

if k+a < d or d == 0:
    print("hasu")
else:
    print("gosu")