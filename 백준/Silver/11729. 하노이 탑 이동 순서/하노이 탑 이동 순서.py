from sys import stdin

def hanoi(num, frm, to, other):
    global answer
    global count
    if num == 0:
        return
    hanoi(num-1, frm, other, to)
    # 1 1 3 2
    answer.append([frm, to])
    hanoi(num - 1, other, to, frm)
    count += 1

n = int(stdin.readline())
answer = []
frm = 1
to = 3
other = 2
count = 0
hanoi(n, frm, to, other)
print(count)
for i in range(len(answer)):
    print(answer[i][0], answer[i][1])
