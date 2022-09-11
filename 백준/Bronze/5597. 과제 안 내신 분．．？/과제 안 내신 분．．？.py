from sys import stdin

li = [0]*31
for i in range(28):
  a = int(stdin.readline())
  li[a] += 1

for i in range(1, 31):
  if li[i] == 0:
    print(i)