from sys import stdin

X = int(stdin.readline())
i, num = 0, 0
while X > num:
    i += 1
    num += i

# print(i, num, X - (num - i))
# 짝수 줄 -> 분모가 내림차순
if i % 2 == 0:
    # i = 4, num = 10, X = 10
    a = X - (num - i)
    b = i - (X - (num - i)) + 1
    #a = 1 to i
    #b = i to 1
# 홀수 줄 -> 분모가 오름차순
else:
    a = i - (X - (num - i)) + 1
    b = 1 + (X - (num - i)) - 1

print(str(a) + "/" + str(b))
