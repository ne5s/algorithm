from sys import stdin

while True:
    a, b, c = map(int, stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a>b>c or a>c>b:
        if a**2 == b**2 + c**2:
            print("right")
        else:
            print("wrong")
    elif b>a>c or b>c>a:
        if b**2 == a**2 + c**2:
            print("right")
        else:
            print("wrong")
    if c>a>b or c>b>a:
        if c**2 == a**2 + b**2:
            print("right")
        else:
            print("wrong")
