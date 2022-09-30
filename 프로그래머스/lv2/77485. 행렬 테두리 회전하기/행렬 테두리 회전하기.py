def solution(rows, columns, queries):
    answer = []
    li = [[0] * columns  for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            li[i][j] = cnt
            cnt += 1
    # print(li)

    for query in queries:
        query = [x-1 for x in query]
        x1,y1,x2,y2 = query
        # print(x1,y1,x2,y2)
        tmp = li[x1][y1]
        small = tmp

        # left
        for i in range(x1+1, x2+1):
            li[i-1][y1] = li[i][y1]
            small = min(small, li[i][y1])

        # bottom
        for i in range(y1+1, y2+1):
            li[x2][i-1] = li[x2][i]
            small = min(small, li[x2][i])

        # right
        for i in range(x2-1, x1-1, -1):
            li[i+1][y2] = li[i][y2]
            small = min(small, li[i][y2])

        # top
        for i in range(y2-1, y1-1, -1):
            li[x1][i+1] = li[x1][i]
            small = min(small, li[x1][i])

        li[x1][y1+1] = tmp

        answer.append(small)


    return answer