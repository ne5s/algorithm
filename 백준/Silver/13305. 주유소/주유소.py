from sys import stdin

N = int(stdin.readline())
adj_road_len = list(map(int, stdin.readline().split()))
juyouso = list(map(int, stdin.readline().split()))

min_money= 0
m = juyouso[0]
for i in range(len(adj_road_len)):
    if juyouso[i] < m:
        m = juyouso[i]
    min_money += m * adj_road_len[i]

print(min_money)