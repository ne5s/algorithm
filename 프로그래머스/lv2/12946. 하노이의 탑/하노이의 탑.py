answer = []
def hanoi(num, frm, to, other):
    global answer
    if num == 0:
        return
    hanoi(num-1, frm, other, to)
    answer.append([frm, to])
    hanoi(num - 1, other, to, frm)

def solution(n):
    frm = 1
    to = 3
    other = 2
    hanoi(n, frm, to, other)
    return answer