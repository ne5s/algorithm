from sys import stdin

n,k = list(map(int,stdin.readline().split()))
def factorial(n):
    if n ==0 or n==1:
        return 1
    a = 1
    for i in range(2, n+1):
        a *= i
    return a
print(factorial(n) // factorial(k) // factorial(n-k))




