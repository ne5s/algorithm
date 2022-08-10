from sys import stdin
def hansu(n):
    if(n<100):
        return True
    if(n//100 - n%100//10 == n%100//10 - n%10):
        return True
    else:
        return False

N = int(stdin.readline())
li = [False]*N
cnt = 0
for i in range(1, len(li)+1):
    li[i-1] = hansu(i)
    if li[i-1]:
        cnt += 1
print(cnt)