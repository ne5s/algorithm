from sys import stdin

N, K = map(int, stdin.readline().split())
li = list(map(int, stdin.readline().split()))
partial_sum = sum(li[:K])
sum_arr = [partial_sum]

for i in range(0, N-K):
    partial_sum = partial_sum - li[i] + li[i+K]
    sum_arr.append(partial_sum)

print(max(sum_arr))