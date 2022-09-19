# import math

# def dateToMinutes(date):
#     h, m = map(int, date.split(':'))
#     return h*60 + m
    
# def solution(fees, records):
#     answer = []

#     # 기본 시간, 기본 요금, 단위 시간, 단위 요금 순
#     dt, df, ut, uf = fees
    
#     dic = dict()

#     for r in records:
#         time, number, history = r.split()
#         number = int(number)
        
#         if number in dic:
#             dic[number].append([dateToMinutes(time), history])
#         else:
#             dic[number] = [[dateToMinutes(time), history]]
    
#     rList = list(dic.items())
#     rList.sort(key=lambda x : x[0])
    
#     for r in rList:
#         t = 0

#         for rr in r[1]:
#             if rr[1] == "IN":
#                 t -= rr[0]
#             else:
#                 t += rr[0]

#         if r[1][-1][1] == "IN":
#             t += dateToMinutes('23:59')
        
#         if t <= dt:
#             answer.append(df)
#         else:
#             answer.append(df + math.ceil((t-dt) / ut) * uf)        

#     return answer
# ---------------
import math


def solution(fees, records):
    car_num = set()
    result = []
    answer = []
    # print(records)
    for i in range(len(records)):
        time, car, case = records[i].split()
        # print("records[i]:",time,car,case)
        if case == "IN":
            for j in range(len(records)):
                time2, car2, case2 = records[j].split()
                if car2 == car and case2 == "OUT":
                    h1 = int(time.split(':')[0])
                    m1 = int(time.split(':')[1])
                    h2 = int(time2.split(':')[0])
                    m2 = int(time2.split(':')[1])
                    minute = (h2-h1)*60 + (m2-m1)
                    if car in car_num:
                        for ans in range(len(result)):
                            if result[ans][0] == car:
                                result[ans][1] += minute
                    else:
                        result.append([car, minute])
                    records[i] = records[i].replace("IN", "check")
                    records[j] = records[j].replace("OUT", "check")
                    car_num.add(car)
                    break

    car_num = list(car_num)
    car_num = list(map(int, car_num))
    car_num.sort()
    for i in range(len(car_num)):
        car_num[i] = str(car_num[i]).zfill(4)
    # print(result)
    for i in records:
        time, car, case = i.split()
        if case == "IN":
            if car in car_num:
                for j in range(len(result)):
                    if result[j][0] == car:
                        h1 = int(time.split(':')[0])
                        m1 = int(time.split(':')[1])
                        h2 = 23
                        m2 = 59
                        minute = (h2 - h1) * 60 + (m2 - m1)
                        result[j][1] += minute
                        break
            else:
                h1 = int(time.split(':')[0])
                m1 = int(time.split(':')[1])
                h2 = 23
                m2 = 59
                minute = (h2 - h1) * 60 + (m2 - m1)
                car_num.append(car)
                result.append([car, minute])

    car_num = list(car_num)
    car_num = list(map(int, car_num))
    car_num.sort()
    for i in range(len(car_num)):
        car_num[i] = str(car_num[i]).zfill(4)

    print(car_num)
    # print(records)
    print("result:", result)

    for c in car_num:
        for r in result:
            if r[0] == c:
                if r[1] <= fees[0]:
                    answer.append(fees[1])
                else:
                    answer.append(fees[1] + math.ceil( (r[1]-fees[0])/fees[2] ) * fees[3] )

    return answer