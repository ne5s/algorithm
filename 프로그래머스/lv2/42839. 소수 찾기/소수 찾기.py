import math
from itertools import permutations

def is_prime(n):
    if n==0 or n==1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_arr = []
    prime_number = []
    for i in numbers:
        num_arr.append(int(i))
    length = len(num_arr)
    # 길이 1
    for i in num_arr:
        if is_prime(i) and i not in prime_number:
            prime_number.append(i)
    # 길이 2
    if length < 2:
        pass
    else:
        li = list(permutations(num_arr, 2))
        for i in li:
            num = 10*i[0] + i[1]
            if is_prime(num) and num not in prime_number:
                prime_number.append(num)
    # 길이 3
    if length < 3:
        pass
    else:
        li = list(permutations(num_arr, 3))
        for i in li:
            num = 100*i[0] + 10*i[1] + i[2]
            if is_prime(num) and num not in prime_number:
                prime_number.append(num)
    # 길이 4
    if length < 4:
        pass
    else:
        li = list(permutations(num_arr, 4))
        for i in li:
            num = 1000*i[0] + 100*i[1] + 10*i[2] + i[3]
            if is_prime(num) and num not in prime_number:
                prime_number.append(num)
    # 길이 5
    if length < 5:
        pass
    else:
        li = list(permutations(num_arr, 5))
        for i in li:
            num = 10000*i[0] + 1000*i[1] + 100*i[2] + 10*i[3] + i[4]
            if is_prime(num) and num not in prime_number:
                prime_number.append(num)
    # 길이 6
    if length < 6:
        pass
    else:
        li = list(permutations(num_arr, 6))
        for i in li:
            num = 100000*i[0] + 10000*i[1] + 1000*i[2] + 100*i[3] + 10* i[4] + i[5]
            if is_prime(num) and num not in prime_number:
                prime_number.append(num)
    # 길이 7
    if length < 7:
        pass
    else:
        li = list(permutations(num_arr, 7))
        for i in li:
            num = 1000000*i[0] + 100000*i[1] + 10000*i[2] + \
                  1000*i[3] + 100* i[4] + 10 * i[5] + i[6]
            if is_prime(num) and num not in prime_number:
                prime_number.append(num)


    answer = len(prime_number)
    return answer