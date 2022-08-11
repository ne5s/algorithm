from sys import stdin

A, B = stdin.readline().split()
reversed_A = ''
reversed_B = ''
for i in reversed(range(len(A))):
    reversed_A += A[i]
    reversed_B += B[i]
if int(reversed_A) > int(reversed_B):
    print(reversed_A)
else:
    print(reversed_B)