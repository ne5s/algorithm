def solution(N, number):
    answer = -1
    dp = []
    # return 값이 8보다 크면 -1을 return하게 하므로 8까지만 확인한다
    for i in range(1, 9):
        check_list = set()
        # 1~8자리의 N을 검사하도록 넣어준다. ex) N이 2일 때 return이 2려면 number가 22
        check_list.add(int(str(N)*i))
        # i가 1일 때는 반복문을 안돌리기 위해..
        # dp[0]과는 무조건 dp[-1]을 붙여줘야 return 2인 dp에서 dp3을 찾을 수 있음
        for j in range(0, i-1):
            for op1 in dp[j]:
                for op2 in dp[-1-j]:
                    check_list.add(op1 - op2)
                    check_list.add(op1 + op2)
                    check_list.add(op1 * op2)
                    if op2 != 0:
                        check_list.add(op1 // op2)

        if number in check_list:
            answer = i
            break
            
        dp.append(check_list)

    return answer