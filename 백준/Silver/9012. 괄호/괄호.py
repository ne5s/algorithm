from sys import stdin

n = int(stdin.readline())
for i in range(n):
    st = []
    flag = 0
    a = stdin.readline().rstrip()
    for j in a:
        if j == "(":
            st.append(j)
        else:
            if len(st) == 0:
                flag = 1
                break
            st.pop()
    if len(st) == 0 and flag == 0:
        print("YES")
    else:
        print("NO")

