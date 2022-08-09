from sys import stdin

li = [0]*9
for i in range(9):
    li[i] = int(stdin.readline())

max = max(li)
idx = li.index(max)
print(str(max) +  '\n' +  str(idx+1))

