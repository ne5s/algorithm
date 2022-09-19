from collections import deque

def bfs(n, info):
    # 최대 점수차를 만든 화살 상황을 저장하는 리스트
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    # 최대 점수 차
    maxGap = 0

    while q:
        # focus : 지금 몇 점에 화살을 쏠 건지
        # arrow : 현재 화살 상황
        # info -> 어치피가 쏜 것, arrow -> 라이언이 쏜 것
        focus, arrow = q.popleft()
        # print("focus:", focus, "arrow:", arrow)

        # 종료조건 1 : 화살을 다 쐈을 때
        if sum(arrow) == n:
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0): # 둘 다 하나도 못맞췄으면 서로 점수 없으므로
                    if info[i] >= arrow[i]: # 어피치가 라이언보다 같거나 많이 쐈으면
                        apeach += (10-i) # 어피치에 해당 점수를 더해줌
                    else:
                        lion += (10-i) # 라이언이 더 많이 쐈으면 라이언 점수 올려줌
            if apeach < lion:
                # 점수 차 계산
                gap = lion - apeach
                # 이전 최대 점수 차가 더 크다면 이 경우, 넘어감
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap # 최대 점수 차 갱신 및 저장하는 리스트 초기화
                    res.clear()
                res.append(arrow) # 최대 점수차를 내는 화살 상황 저장

        elif sum(arrow) > n: # 종료조건 2 : 화살을 n개보다 더 쐈을 경우
            continue

        elif focus == 10: # 종료조건 3 : 화살을 덜 쏜 경우 # (마지막 화살 상황까지 왔는데 sum(arrow)가 n보다 작음)
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))

        # 화살 쏘는 상황
        # 어피치를 이기려면, 해당 과녁에 1개 더 쏘거나
        # 해당 과녁에서 안 쏘고, 다른 과녁에서 더 이기거나
        else:
            tmp = arrow.copy()
            tmp[focus] = info[focus] + 1
            q.append((focus + 1, tmp))  # 어피치보다 1발 많이 쏘기

            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus + 1, tmp2))  # 해당 과녁에서 안 쏘기

    return res

def solution(n, info):
    winList = bfs(n, info)
    print(winList)
    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]