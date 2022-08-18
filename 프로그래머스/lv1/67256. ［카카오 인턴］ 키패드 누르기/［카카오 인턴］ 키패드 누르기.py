def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            left = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            right = i
        else: # 2,5,8,0
            l_dis = 0
            r_dis = 0
            if i == 0:
                i = 11
            if abs(i-left) == 1 or abs(i-left) == 3:
                l_dis = 1
            elif abs(i-left) == 4 or abs(i-left) == 2 or abs(i-left) == 6:
                l_dis = 2
            elif abs(i-left) == 7 or abs(i-left) == 5 or abs(i-left) == 9:
                l_dis = 3
            elif abs(i-left) == 10 or abs(i-left) == 8:
                l_dis = 4
            if abs(i-right) == 1 or abs(i-right) == 3:
                r_dis = 1
            elif abs(i-right) == 2 or abs(i-right) == 4 or abs(i-right) == 6:
                r_dis = 2
            elif abs(i-right) == 5 or abs(i-right) == 7 or abs(i-right) == 9:
                r_dis = 3
            elif abs(i-right) == 8 or abs(i-right) == 10:
                r_dis = 4
            if l_dis == r_dis:
                if hand == 'right':
                    answer += 'R'
                    if i == 11:
                        right = 11
                    else:
                        right = i
                elif hand == 'left':
                    answer += 'L'
                    if i == 11:
                        left = 11
                    else:
                        left = i
            else:
                if l_dis < r_dis:
                    answer += 'L'
                    if i == 11:
                        left = 11
                    else:
                        left = i
                elif l_dis > r_dis:
                    answer += 'R'
                    if i == 11:
                        right = 11
                    else:
                        right = i
    return answer