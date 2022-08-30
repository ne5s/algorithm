from sys import stdin

n = int(stdin.readline())
max = 0
for i in range(n):
    a = stdin.readline().rstrip()
    for_num = a.count("for")
    while_num = a.count("while")
    if max < for_num+while_num:
        max = for_num+while_num
print(max)