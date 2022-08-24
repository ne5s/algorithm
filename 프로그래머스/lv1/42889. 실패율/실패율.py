def solution(N, stages):
    answer = []
    silpae = {}
    dodal = {}
    user_count = len(stages)
    for i in range(1, N+1):
        silpae[i] = 0
        dodal[i] = 0
    for j in stages:
        if j == N+1:
            for o in range(1, N+1):
                dodal[o] += 1
        else:
            for o in range(1, j+1):
                dodal[o] += 1
            silpae[j] += 1
    for i in range(1, len(silpae)+1):
        if dodal[i] == 0:
            silpae[i] = 0
        else:
            silpae[i] = silpae[i] / dodal[i]
    sorted_silpae = sorted(silpae.items(), key = lambda item : item[1], reverse=True)
    for i in sorted_silpae:
        answer.append(i[0])
    return answer