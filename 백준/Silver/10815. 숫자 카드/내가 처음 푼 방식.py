from sys import stdin

n = int(stdin.readline())
sol = list(map(int, stdin.readline().split()))
if len(sol) != n:
    print("잘못된 입력입니다.")
m = int(stdin.readline())
ipt = list(map(int, stdin.readline().split()))
if len(ipt) != m:
    print("잘못된 입력입니다.")
    
sol.sort()
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
    
for i in range(m):
    if binary_search(sol, ipt[i], 0, n-1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
