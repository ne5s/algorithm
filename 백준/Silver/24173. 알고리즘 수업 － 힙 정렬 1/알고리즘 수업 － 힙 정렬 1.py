from sys import stdin

def heap_sort(li, n):
    global cnt
    build_min_heap(li, n)
    for i in range(n, 1, -1):
        li[1], li[i] = li[i], li[1]
        cnt += 1
        if cnt == K:
            print(li[i], li[1])
            exit()
        heapify(li, 1, i-1)

def build_min_heap(li, n):
    for i in range(n//2, 0, -1):
        heapify(li, i, n)

def heapify(li, k, n):
    global cnt
    left = 2 * k
    right = 2 * k + 1
    if right <= n:
        if li[left] < li[right]:
            smaller = left
        else:
            smaller = right
    elif left <= n:
        smaller = left
    else:
        return

    if li[smaller] < li[k]:
        li[k], li[smaller] = li[smaller], li[k]
        cnt += 1
        if cnt == K:
            print(li[k], li[smaller])
            exit()
        heapify(li, smaller, n)

N, K = map(int, stdin.readline().split())
li = [0] + list(map(int, stdin.readline().split()))
cnt = 0
heap_sort(li, N)
print(-1)