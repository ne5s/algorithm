from itertools import combinations
def solution(numbers):
    answer = []
    combi = list(combinations(numbers, 2))
    for i in combi:
        if sum(i) not in answer:
            answer.append(sum(i))
            
    return sorted(answer)