from sys import stdin

while True:
    a = stdin.readline().rstrip()
    li = []
    flag = True
    if a == '.':
        break
    for i in a:
        if i == "(" or i == "[":
            li.append(i)
        elif i == "]":
            if len(li) == 0 or li[-1] != "[":
                flag = False
                break
            last = li.pop()
            if last == "[":
                continue
        elif i == ")":
            if len(li) == 0 or li[-1] != "(":
                flag = False
                break
            last = li.pop()
            if last == "(":
                continue
    if flag and len(li) == 0:
        print("yes")
    else:
        print("no")