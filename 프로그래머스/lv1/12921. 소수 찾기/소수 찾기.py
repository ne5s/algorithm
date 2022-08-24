import math

def solution(n):
    answer = 0
    for i in range(1, n+1):
        flag = 0
        if i == 1:
            continue
        else:
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    flag = 1
                    break
        if flag == 0:
            answer += 1
    return answer