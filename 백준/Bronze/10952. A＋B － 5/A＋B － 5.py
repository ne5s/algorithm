from sys import stdin

while True:
    a, b = list(map(int, stdin.readline().split()))
    if(a == 0 and b == 0):
        break
    print(a+b)