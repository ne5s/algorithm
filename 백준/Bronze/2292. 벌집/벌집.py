from sys import stdin

N = int(stdin.readline())
cnt = 1
vsnum = 1
while vsnum < N:
    vsnum = vsnum + 6 * cnt
    cnt += 1

print(cnt)