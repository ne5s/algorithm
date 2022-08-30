def solution(price, money, count):
    answer = 0
    pay = 0
    for i in range(count):
        pay += (price * (i+1))
    
    
    return (pay-money if pay>money else 0)