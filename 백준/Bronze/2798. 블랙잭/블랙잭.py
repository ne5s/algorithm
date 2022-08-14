from sys import stdin
from itertools import *

n,m = list(map(int,stdin.readline().split()))
li = list(map(int,stdin.readline().split()))
three_combi = list(combinations(li, 3))
result = 0
for i in three_combi:
    if sum(i) <= m and sum(i) >= result:
        result = sum(i)

print(result)