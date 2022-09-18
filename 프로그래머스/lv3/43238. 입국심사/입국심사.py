def solution(n, times):
    # times.sort()
    start = 1
    end = times[-1]*n
    result = end

    # 여기서 mid가 심사 받는 데 걸리는 시간이 됨
    while start <= end:
        mid = (start+end) // 2
        # 30 / 7 = 4, 30 / 10 = 3 , 30분에 7명
        people = 0
        for time in times:
            people += (mid // time)

        if people < n:
            start = mid+1
        else:
        # 이 경우가 심사할 수 있는 사람 수가 n과 같거나 n보다 많기에
        # 결과에 반영해줘야 함
            end = mid-1
            result = min(result, mid)

    return result