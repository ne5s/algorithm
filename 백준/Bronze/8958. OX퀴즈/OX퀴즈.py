from sys import stdin

n = int(stdin.readline())
for i in range(n):
    flag = 0
    sum = 0
    text = stdin.readline()
    for j in text:
        if j == "O":
            flag += 1
            sum += flag
        elif j == "X":
            flag = 0
    print(sum)
