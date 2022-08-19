def solution(s):
    answer = True
    flag = 0
    stack = []
    for i in range(len(s)):
        if i == 0 and s[i] == ")":
            return False
        if s[i] == "(":
            flag += 1
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            poped = stack.pop()
            if poped != "(":
                return False
            flag -= 1
    if flag == 0 and len(stack) == 0:
        pass
    else:
        answer = False
    return answer