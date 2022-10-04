import math
from sys import stdin

N = int(stdin.readline().rstrip())
li = list(map(int, stdin.readline().split()))
cnt = 0

def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for i in li:
    if isPrime(i):
        cnt += 1

print(cnt)