def solution(participant, completion):
    answer = ''
    p_dic = {}
    for i in participant:
        if i in p_dic:
            p_dic[i] += 1
        else:
            p_dic[i] = 1
    for i in completion:
        p_dic[i] -= 1

    for k,v in p_dic.items():
        if v == 1:
            answer = k

    return answer