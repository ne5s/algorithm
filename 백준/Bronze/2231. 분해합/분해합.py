from sys import stdin

n = int(stdin.readline().rstrip())
min = 0

for i in range(1, n):
    9876543
    a = i // 1000000 # 9
    a1 = i % 1000000 # 876543
    b = a1 // 100000 # 8
    b1 = a1 % 100000 # 76543
    c = b1 // 10000 # 7
    c1 = b1 % 10000 # 6543
    d = c1 // 1000 # 6
    d1 = c1 % 1000 # 543
    e = d1 // 100 # 5
    e1 = d1 % 100 # 43
    f = e1 // 10 # 4
    g = e1 % 10 # 3
    want = i + a + b + c + d + e + f + g
    if want == n:
        if min == 0:
            min = i
        elif min > want:
            min = i
print(min)