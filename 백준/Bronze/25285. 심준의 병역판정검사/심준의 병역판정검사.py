from sys import stdin

n = int(stdin.readline())
for i in range(n):
    h, w = map(int,stdin.readline().split())
    if h < 140.1:
        print(6)
    elif 140.1 <= h and h <146:
        print(5)
    elif 146<= h and h<159:
        print(4)
    elif 159<=h and h<161:
        bmi = w / (h/100) / (h/100)
        if 16.0<=bmi and bmi<35.0:
            print(3)
        else:
            print(4)
    elif 161<=h and h<204:
        bmi = w / (h / 100) / (h / 100)
        if 20.0<=bmi and bmi<25.0:
            print(1)
        elif (18.5<=bmi and bmi<20.0) or (25.0<=bmi and bmi<30.0):
            print(2)
        elif (16.0<=bmi and bmi<18.5) or (30.0<=bmi and bmi<35.0):
            print(3)
        else:
            print(4)
    else:
        print(4)