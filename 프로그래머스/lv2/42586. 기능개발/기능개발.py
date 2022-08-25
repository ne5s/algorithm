from collections import deque
def solution(progresses, speeds):
    answer = []
    dq = deque()
    for i in progresses:
        dq.append(i)
    day = 1
    index = 0
    baepo = 0
    todo = 0
    while index < len(speeds):
        if todo == 0:
            todo = dq.popleft()
        if todo + (day*speeds[index]) >= 100:
            baepo += 1
            index += 1
            todo = 0
        elif baepo == 0:
            day += 1
        elif baepo != 0:
            answer.append(baepo)
            baepo = 0
            day += 1
    answer.append(baepo)
    return answer