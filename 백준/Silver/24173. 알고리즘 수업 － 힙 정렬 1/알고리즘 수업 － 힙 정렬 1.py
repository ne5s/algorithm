from sys import stdin

n, k = map(int, stdin.readline().split())
li = [0]
a = list(map(int, stdin.readline().split()))
for i in a:
    li.append(i)
cnt = 0
small = []

def heap_sort(li):
    global cnt
    build_min_heap(li)
    for i in range(n, 1, -1):
        cnt += 1
        small.append([min(li[i], li[1]), max(li[i], li[1])])
        li[1], li[i] = li[i], li[1]
        heapify(li, 1, i-1)

def build_min_heap(li):
    for i in range(n//2, 0, -1):
        heapify(li, i, n)

def heapify(li, k, n):
    global cnt
    global small
    left = 2 * k
    right = 2 * k + 1
    if (right <= n):
        if li[left] < li[right]:
            smaller = left
        else:
            smaller = right
    elif left <= n:
        smaller = left
    else:
        return

    if li[smaller] < li[k]:
        cnt += 1
        small.append([li[smaller], li[k]])
        li[k], li[smaller] = li[smaller], li[k]
        heapify(li, smaller, n)

    return

heap_sort(li)
if k > cnt:
    print(-1)
else:
    print(small[k-1][0], small[k-1][1])