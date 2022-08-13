from itertools import *

def solution(nums):
    answer = 0

    if len(nums) == 3:
        answer += is_prime_number(sum(nums))
    else:
        three_value = list(combinations(nums, 3))
        for i in three_value:
            answer += is_prime_number(sum(i))
    return answer

def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return 0 # 소수가 아님
    return 1 # 소수임