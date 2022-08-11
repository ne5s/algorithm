from sys import stdin

T = int(stdin.readline())
for i in range(T):
    R, S = stdin.readline().split()
    R = int(R)
    for j in S:
        print(j * R, end='')
    print()