def solution(n):
    third_jin = ''
    while n>0:
        n, mod = divmod(n, 3)
        third_jin += str(mod)
    return int(third_jin, 3)