from sys import stdin

def bin_search(arr, want, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == want:
        return mid
    elif arr[mid] > want:
        return bin_search(arr, want, start, mid-1)
    else:
        return bin_search(arr, want, mid+1, end)

n = int(stdin.readline().rstrip())
a = list(map(int, stdin.readline().rstrip().split()))
m = int(stdin.readline().rstrip())
b = list(map(int, stdin.readline().rstrip().split()))

a.sort()
for i in b:
    result = bin_search(a, i, 0, n-1)
    if result == None:
        print(0)
    else:
        print(1)