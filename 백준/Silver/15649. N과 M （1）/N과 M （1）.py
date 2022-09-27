from sys import stdin
from itertools import permutations
N, M = map(int, stdin.readline().split())
P = permutations(range(1, N+1), M)  # iter(tuple)

for i in P:
    print(' '.join(map(str, i)))  # tuple -> str