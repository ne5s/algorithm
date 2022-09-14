from sys import stdin

s = stdin.readline().rstrip()

act0 = 0
act1 = 0

if s[0] == '1':
    act0 += 1
else:
    act1 += 1
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            act0 += 1
        else:
            act1 += 1
print(min(act0, act1))