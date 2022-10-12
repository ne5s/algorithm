from sys import stdin

N = int(stdin.readline())
cnt = 1
a = 666
while cnt != N:
    a += 1
    if '666' in str(a):
        cnt += 1

print(a)
