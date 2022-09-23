def solution(board, skill):
    answer = 0
    li = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    # 누적합 기록을 위한 배열

    for type, r1, c1, r2, c2, degree in skill:
        li[r1][c1] += degree if type == 2 else -degree
        li[r1][c2+1] += -degree if type == 2 else degree
        li[r2+1][c1] += -degree if type == 2 else degree
        li[r2+1][c2+1] += degree if type == 2 else -degree

    # 행 기준 누적합
    for i in range(len(li)-1):
        for j in range(len(li[0])-1):
            li[i][j+1] += li[i][j]

    # 열 기준 누적합
    for j in range(len(li[0]) - 1):
        for i in range(len(li) - 1):
            li[i + 1][j] += li[i][j]

    # 기존 배열과 합함
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += li[i][j]
            # board에 값이 1이상인 경우 answer++
            if board[i][j] > 0: answer += 1

    return answer