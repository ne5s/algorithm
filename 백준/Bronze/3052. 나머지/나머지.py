from sys import stdin

li = [0]*10
for i in range(10):
    li[i] = int(stdin.readline())

rest = [0]*42
for i in range(len(li)):
    rest[(li[i] % 42)] += 1

flag = 0
for i in range(len(rest)):
    if(rest[i] != 0):
        flag += 1
print(flag)
