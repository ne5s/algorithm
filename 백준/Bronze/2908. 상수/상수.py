from sys import stdin

A, B = stdin.readline().split()
reversed_A = A[::-1]
reversed_B = B[::-1]
print(max(reversed_A, reversed_B))
