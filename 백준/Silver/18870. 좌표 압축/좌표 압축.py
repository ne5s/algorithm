from sys import stdin

N = int(stdin.readline())
li = list(map(int, stdin.readline().split()))
sorted_li = list(sorted(set(li)))
ranked_li = {sorted_li[i]: i for i in range(len(sorted_li))}
print(*[ranked_li[i] for i in li])