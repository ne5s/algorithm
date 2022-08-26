import math

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        yaksu = 0
        for j in range(1, i+1):
            # if i == j*j:
                # yaksu += 1
            # elif i % j == 0:
                # yaksu += 2
            if i % j == 0:
                yaksu += 1
        if yaksu % 2 ==0:
            answer += i
        else:
            answer -= i
    return answer