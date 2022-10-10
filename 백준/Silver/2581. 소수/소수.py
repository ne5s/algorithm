import math
from sys import stdin

def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

M = int(stdin.readline())
N = int(stdin.readline())
sum = 0
min_sosu = N+1
for i in range(M, N+1):
    if isPrime(i):
        sum += i
        min_sosu = min(min_sosu, i)

if min_sosu == N+1:
    print(-1)
else:
    print(sum)
    print(min_sosu)
