from sys import stdin

def fib(n):
    global re
    if n == 1 or n == 2:
        re += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_dp(n):
    global fibo
    li[1], li[2] = 1,1
    for i in range(3, n+1):
        fibo += 1
        li[n] = li[n-1] + li[n-2]
    return li[n]


li = [0]*41
re = 0
fibo = 0

n = int(stdin.readline())
a = fib(n)
b = fib_dp(n)
print(re, fibo)