def self_number(n):
    if(n < 10):
        return n+n
    elif(n>=10 and n<100):
        return n + int(str(n)[0]) + int(str(n)[1])
    elif(n>=100 and n<1000):
        return n + int(str(n)[0]) + int(str(n)[1]) + int(str(n)[2])
    elif(n>=1000 and n<10000):
        return n + int(str(n)[0]) + int(str(n)[1]) + int(str(n)[2]) + int(str(n)[3])
    elif(n == 10000):
        return n + int(str(n)[0]) + int(str(n)[1]) + int(str(n)[2]) + int(str(n)[3]) + int(str(n)[4])
    
self_number_li = []
for i in range(1, 10001):
    self_number_li.append(self_number(i))
for j in range(1, 10001):
    if j not in self_number_li:
        print(j)

