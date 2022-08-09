from sys import stdin

while True:
    try:
        a, b = list(map(int, stdin.readline().split()))
        print(a+b)
    except:
        break