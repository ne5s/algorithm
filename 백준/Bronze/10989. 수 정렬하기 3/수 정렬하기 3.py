from sys import stdin

n = int(stdin.readline())
num_count = [0] * 10001
for _ in range(n):
    num_count[int(stdin.readline())] += 1

for i in range(1, 10001):
    if num_count[i] > 0:
        for _ in range(num_count[i]):
            print(i)