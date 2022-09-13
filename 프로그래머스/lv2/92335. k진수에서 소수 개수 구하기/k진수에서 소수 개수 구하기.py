import math

def njinsu(n, q):
    word = ''
    while n>0:
        n, mod = divmod(n, q)
        word = str(mod) + word

    return word


def solution(n, k):
    jinsu_num = njinsu(n,k)
    jinsu_num = jinsu_num.split('0')

    count = 0
    for p in jinsu_num:
        # 00이 중복되면 0으로 split했을 때 빈공간이 남아버린다. -> len(p) == 0
        if len(p) == 0 or int(p) == 1:
            continue
        isPrime = True
        for i in range(2, int(math.sqrt(int(p)))+1):
            if int(p) % i == 0:
                isPrime = False
                break
        if isPrime:
            count += 1
    return count