def solution(board, moves):
    answer = 0
    sero = []
    basket = []
    for j in range(len(board)):
        sero_one = []
        for i in (range(len(board))):
            sero_one.append(board[i][j])
        sero.append(sero_one)
    for i in moves:
        for j in range(len(board)):
            if sero[i-1][j] != 0:
                if len(basket) == 0:
                    basket.append(sero[i-1][j])
                elif len(basket) != 0 and basket[-1] != sero[i-1][j]:
                    basket.append(sero[i-1][j])
                else:
                    del basket[-1]
                    answer += 2
                sero[i-1][j] = 0
                break
    return answer