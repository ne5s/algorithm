from sys import stdin

S = stdin.readline().rstrip()
li = set()
for i in range(len(S)):
    substr = S[i]
    li.add(substr)
    for j in range(i+1, len(S)):
        substr += S[j]
        li.add(substr)
print(len(li))
