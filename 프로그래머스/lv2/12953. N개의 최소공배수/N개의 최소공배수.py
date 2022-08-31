import math
def solution(arr):
    lcms = sorted(arr)
    while len(lcms) != 1:
        change = []
        for i in range(1, len(lcms)):
            gcd = math.gcd(lcms[0], lcms[i])
            lcm = gcd * (lcms[0]/gcd) * (lcms[i]/gcd)
            change.append(int(lcm))
        lcms = change

    return lcms[0]