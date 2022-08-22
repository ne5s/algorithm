from sys import stdin

a, b= list(map(int, stdin.readline().split()))
while a !=0 and b != 0:
    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")
    a, b = list(map(int, stdin.readline().split()))


