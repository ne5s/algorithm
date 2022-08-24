from sys import stdin

a,b  = list(map(int,stdin.readline().split()))
def gcd(a,b):
    while b>0:
        tmp = a
        a = b
        b = tmp % b
    return a

print(gcd(a,b))
print(int(a*b/gcd(a,b)))



