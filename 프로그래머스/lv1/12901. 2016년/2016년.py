def solution(a, b):
    yoil = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # a = 1, b = 1
    # a = 3, b = 1

    for i in range(a-1):
        b += days[i]

    return yoil[(b-1) % 7]