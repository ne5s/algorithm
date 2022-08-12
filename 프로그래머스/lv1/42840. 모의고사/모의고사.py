def solution(answers):
    answer = []
    answer_count = [0]*3
    n = len(answers)
    one = [1,2,3,4,5]* (n//5) + [1,2,3,4,5][:n%5]
    two = [2,1,2,3,2,4,2,5] * (n//8) + [2,1,2,3,2,4,2,5][:n%8]
    three = [3,3,1,1,2,2,4,4,5,5]* (n//10) + [3,3,1,1,2,2,4,4,5,5][:n%10]
    for i in range(n):
        if one[i] == answers[i]:
            answer_count[0] += 1
        if two[i] == answers[i]:
            answer_count[1] += 1
        if three[i] == answers[i]:
            answer_count[2] += 1
    m = max(answer_count)
    answer = [i+1 for i,v in enumerate(answer_count) if v == m]
    return answer