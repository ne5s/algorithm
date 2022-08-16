def solution(lottos, win_nums):
    answer = []
    flag = 0
    zero_l = 0
    for i in lottos:
        for j in win_nums:
            if i == 0:
                zero_l += 1
                break
            if i == j:
                flag += 1
                
    best_flag = flag + zero_l
    if best_flag == 2:
        answer.append(5)
    elif best_flag == 3:
        answer.append(4)
    elif best_flag == 4:
        answer.append(3)
    elif best_flag == 5:
        answer.append(2)
    elif best_flag == 6:
        answer.append(1)
    else:
        answer.append(6)

    if flag == 2:
        answer.append(5)
    elif flag == 3:
        answer.append(4)
    elif flag == 4:
        answer.append(3)
    elif flag == 5:
        answer.append(2)
    elif flag == 6:
        answer.append(1)
    else:
        answer.append(6)


    return answer