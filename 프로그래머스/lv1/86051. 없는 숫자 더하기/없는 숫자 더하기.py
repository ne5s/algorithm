def solution(numbers):
    answer = 0
    a = [0,0,0,0,0,0,0,0,0,0]
    for i in numbers:
        a[i] += 1
    for i in range(len(a)):
        if a[i] == 0:
            answer += i
    return answer