from sys import stdin

a = stdin.readline().rstrip()
li = []

for i in a:
    li.append(int(i))

for i in sorted(li, reverse=True):
    print(i, end='')