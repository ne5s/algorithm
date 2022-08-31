from sys import stdin

n = int(stdin.readline())
for i in range(n):
    li = stdin.readline().rstrip().split()
    if li[1] == '+':
        if int(li[0]) + int(li[2]) == int(li[4]):
            print("correct")
        else:
            print("wrong answer")
    elif li[1] == '-':
        if int(li[0]) - int(li[2]) == int(li[4]):
            print("correct")
        else:
            print("wrong answer")
    elif li[1] == '*':
        if int(li[0]) * int(li[2]) == int(li[4]):
            print("correct")
        else:
            print("wrong answer")
    else:
        if int(li[0]) / int(li[2]) == int(li[4]):
            print("correct")
        else:
            print("wrong answer")

