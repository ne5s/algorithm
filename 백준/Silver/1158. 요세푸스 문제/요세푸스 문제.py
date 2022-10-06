from sys import stdin

N, K = map(int, stdin.readline().split())
queue = [i for i in range(1, N+1)]
answer = []
num = 0
while queue:
    num = (num + (K-1)) % len(queue)
    answer.append(str(queue.pop(num)))
print("<", ", ".join(answer), ">", sep='')