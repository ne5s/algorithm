def solution(dartResult):
    i = 0
    st = []
    tmp = -1 # tmp가 -1이면 숫자를 넣어야 한다는 뜻
    while i<len(dartResult):
        if tmp != -1:
            if dartResult[i] == "S":
                tmp = tmp ** 1
            elif dartResult[i] == "D":
                tmp = tmp ** 2
            elif dartResult[i] == "T":
                tmp = tmp ** 3
            elif dartResult[i] == "*":
                if len(st) == 0:
                    tmp = tmp * 2
                    st.append(tmp)
                    tmp = -1
                else:
                    prev = st.pop() * 2
                    tmp = tmp * 2
                    st.append(prev)
                    st.append(tmp)
                    tmp = -1
            elif dartResult[i] == "#":
                tmp = tmp * (-1)
                st.append(tmp)
                tmp = -1
            else: # 다음 숫자가 온 경우
                st.append(tmp)
                tmp = -1
                i -= 1
        else:
            if dartResult[i] == '1':
                if dartResult[i+1] == '0':
                    tmp = 10
                    i += 1
                else:
                    tmp = 1
            else:
                tmp = int(dartResult[i])
        i += 1
    if tmp != -1:
        st.append(tmp)

    return sum(st)