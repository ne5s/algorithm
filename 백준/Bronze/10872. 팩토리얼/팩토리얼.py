from sys import stdin
def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n-1)
n = int(stdin.readline())
print(fac(n))
