from sys import stdin

S = stdin.readline().rstrip()
d = dict()
for i in range(len(S)):
    substr = S[i]
    d[substr] = 0
    for j in range(i+1, len(S)):
        substr += S[j]
        d[substr] = 0
print(len(d))