from sys import stdin

n = int(stdin.readline())
for i in range(n):
    st = []
    flag = 0
    a = stdin.readline().rstrip()
    if flag == 1:
        continue
    for j in range(len(a)):
        if len(st) == 0 and a[j] == ")":
            print("NO")
            flag = 1
            break
        elif a[j] == "(":
            st.append(a[j])
        elif j != 0 and a[j] == ")":
            st.pop()
        if j == len(a)-1 and len(st) == 0:
            print("YES")
        elif j == len(a) -1:
            print("NO")

