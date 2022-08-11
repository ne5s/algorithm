from sys import stdin

N = int(stdin.readline())
sum = 0
for i in range(N):
    a = stdin.readline().rstrip()
    li = []
    flag = True
    for j in range(len(a)):
        if j == 0:
            li.append(a[j])
            continue
        if j != 0 and a[j] not in li:
            li.append(a[j])
        elif j != 0 and a[j] in li and a[j-1] == a[j]:
            li.append(a[j])
        else:
            flag = False
            break
    if flag:
        sum += 1
print(sum)
