def solution(s):
    answer = 0
    alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(alpha)):
        if s.find(alpha[i]) >= 0:
            s = s.replace(alpha[i], str(i))
    answer = int(s)
    return answer