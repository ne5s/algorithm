from sys import stdin
from collections import Counter

N = int(stdin.readline())
li = []
for i in range(N):
    li.append(int(stdin.readline()))
li.sort()

if len(li) == 1:
    many = li[0]
else:
    cnt = Counter(li)
    order = cnt.most_common()
    maximum = order[0][1]
    if order[1][1] == maximum:
        many = order[1][0]
    else:
        many = order[0][0]
print(round(sum(li)/N))
print(li[N//2])
print(many)
print(abs(li[-1] - li[0]))